# Fire Detection

2022년에 화재 영상 탐지를 공부하며 작성한 데이터 처리 노트북과 YOLOv5 실행 코드입니다. 라벨 변환·데이터 분할·학습 명령, 모델 형식 변환, 카메라 추론 코드를 모아두었습니다.

## 저장소에서 확인할 수 있는 것

| 경로 | 내용 |
| --- | --- |
| [Label generate.ipynb](fire_code/Label%20generate.ipynb) | JSON의 box·polygon을 YOLO 좌표로 변환하고 결과를 시각화하는 코드 |
| [Data split.ipynb](fire_code/Data%20split.ipynb) | 이미지 목록을 train/validation/test로 나누고 파일을 이동하는 코드 |
| [yolov5_training_detect.ipynb](fire_code/yolov5_training_detect.ipynb) | YOLOv5 학습·탐지 명령과 ONNX·TorchScript·TFLite 내보내기 기록 |
| [yolov5_dnn.py](fire_code/yolov5_dnn.py) | 카메라 입력, OpenCV DNN 추론, NMS 후처리, 상자 표시와 음성 알림 |
| [Object_detection_file/](Object_detection_file/) | ONNX 파일, 클래스 목록, 추론 코드 사본 |

노트북에는 ONNX·TFLite 변환 성공과 탐지 실행 로그가 남아 있습니다. 원본 PyTorch 가중치와 학습 데이터, 평가 결과 파일 전체는 포함돼 있지 않습니다.

제공된 `coco.names`에는 `fire` 한 클래스가 있습니다. 이 파일만으로 연기까지 구분하는 모델이라고 설명할 수는 없습니다. Jetson에서의 성능 측정, 실시간 처리 보장, 주행·로봇 제어 결과도 이 저장소에서 확인하지 못했습니다.

## 실행 전에 확인할 부분

오래된 경로와 실험 코드가 남아 있어 그대로 전체 실행하기보다 아래 내용을 먼저 확인해야 합니다.

- 추론 코드의 `classesFile`과 `modelWeights`를 현재 위치로 바꾸고, 클래스 목록이 모델 출력과 맞는지 확인합니다.
- 카메라 읽기 실패 시 처리가 없고, 탐지마다 음성 엔진을 초기화해 `runAndWait()`를 호출합니다. 화면에 출력하는 FPS에는 음성 처리 시간도 포함됩니다.
- `json2txt`는 객체마다 클래스와 box·polygon 좌표를 함께 변환해 한 줄씩 저장합니다. 객체가 없으면 빈 파일을 만들고, 좌표가 없는 객체는 위치를 포함한 오류로 알립니다. 기존 class 11 → YOLO class 9 매핑은 유지합니다.
- 분할은 이미지 파일 단위입니다. 같은 영상에서 나온 프레임이 서로 다른 집합에 들어가는지 검사하는 코드는 없습니다.
- 데이터 준비 노트북은 `shutil.move`로 원본 파일을 이동합니다. 복사본에서 경로와 셀을 확인한 뒤 실행해야 합니다.

추론 코드에 필요한 패키지는 `opencv-python`, `numpy`, `pyttsx3`입니다. 카메라·화면 출력·음성 엔진이 필요하며, 이번 정리에서는 이 장치를 연결해 재실행하지 않았습니다. 의존성 버전도 고정돼 있지 않습니다.

## 라벨 변환 테스트

노트북에서 변환 함수만 읽어 임시 JSON과 실제 라벨 파일로 검사합니다. 데이터 이동이나 모델 실행 셀은 실행하지 않습니다.

```bash
python -m unittest discover -s tests -v
```

[테스트 코드](tests/test_label_conversion.py)는 단일 객체, 복수 box, polygon·box 혼합, 빈 주석, 좌표 누락을 확인합니다. 잘못된 주석은 저장 전에 오류를 내므로 기존 라벨 파일을 덮어쓰지 않습니다. 원본 데이터 전체의 라벨을 재생성하거나 모델을 재학습한 검증은 아닙니다.

## 데이터와 참고 자료

- [AI Hub 화재 발생 예측 영상](https://aihub.or.kr/aidata/34121) — 데이터 조사에 참고한 자료
- [AI Hub 열화상 카메라 이미지](https://aihub.or.kr/aidata/27710) — 초기 참고 자료이며, 열화상 모델을 구현했다는 의미는 아닙니다.
- [YOLOv5 학습 참고 글](https://developeryoung.tistory.com/15?category=879762)

독립 평가셋의 탐지 정확도나 오탐률, 장치별 추론 속도를 검증한 수치는 현재 소개에 사용하지 않습니다.
