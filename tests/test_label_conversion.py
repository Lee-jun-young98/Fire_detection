"""노트북의 변환 함수만 읽어 실제 파일 입출력을 검사한다."""

import ast
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "fire_code" / "Label generate.ipynb"


def load_converter():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    namespace = {"json": json}
    names = {"convert", "polygon_Box", "json2txt"}
    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue
        try:
            tree = ast.parse("".join(cell.get("source", [])))
        except SyntaxError:
            continue
        functions = [
            node for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name in names
        ]
        if functions:
            module = ast.Module(body=functions, type_ignores=[])
            exec(compile(module, str(NOTEBOOK), "exec"), namespace)
    return namespace["json2txt"]


class LabelConversionTests(unittest.TestCase):
    def setUp(self):
        self.converter = load_converter()
        self.directory = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.directory.cleanup)
        self.source = Path(self.directory.name) / "annotations.json"
        self.target = Path(self.directory.name) / "labels.txt"

    def write_source(self, annotations):
        payload = {"image": {"resolution": [200, 100]}, "annotations": annotations}
        self.source.write_text(json.dumps(payload), encoding="utf-8-sig")

    def read_labels(self):
        return [
            [float(value) for value in line.split()]
            for line in self.target.read_text(encoding="utf-8").splitlines()
        ]

    def assert_labels(self, expected):
        actual = self.read_labels()
        self.assertEqual(len(actual), len(expected))
        for actual_row, expected_row in zip(actual, expected):
            self.assertEqual(len(actual_row), 5)
            self.assertEqual(actual_row[0], expected_row[0])
            for actual_value, expected_value in zip(actual_row[1:], expected_row[1:]):
                self.assertAlmostEqual(actual_value, expected_value, places=12)

    def test_single_box(self):
        self.write_source([{"class": 1, "box": [20, 10, 60, 30]}])
        self.converter(self.source, self.target)
        self.assert_labels([[0, 0.2, 0.2, 0.2, 0.2]])

    def test_multiple_boxes_keep_class_and_coordinates_together(self):
        self.write_source([
            {"class": 1, "box": [20, 10, 60, 30]},
            {"class": 3, "box": [100, 40, 180, 80]},
        ])
        self.converter(self.source, self.target)
        self.assert_labels([
            [0, 0.2, 0.2, 0.2, 0.2],
            [2, 0.7, 0.6, 0.4, 0.4],
        ])

    def test_mixed_polygon_box_and_existing_class_mapping(self):
        self.write_source([
            {"class": 2, "polygon": [[20, 10], [60, 10], [40, 50]]},
            {"class": 11, "box": [100, 40, 180, 80]},
        ])
        self.converter(self.source, self.target)
        self.assert_labels([
            [1, 0.2, 0.3, 0.2, 0.4],
            [9, 0.7, 0.6, 0.4, 0.4],
        ])

    def test_empty_annotations_write_empty_label_file(self):
        self.write_source([])
        self.target.write_text("old label\n", encoding="utf-8")
        self.converter(self.source, self.target)
        self.assertEqual(self.target.read_text(encoding="utf-8"), "")

    def test_missing_geometry_does_not_reuse_previous_box_or_overwrite_file(self):
        self.write_source([
            {"class": 1, "box": [20, 10, 60, 30]},
            {"class": 2},
        ])
        self.target.write_text("previous labels\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "annotations\\[1\\]"):
            self.converter(self.source, self.target)
        self.assertEqual(self.target.read_text(encoding="utf-8"), "previous labels\n")


if __name__ == "__main__":
    unittest.main()
