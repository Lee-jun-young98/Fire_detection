# Fire Detection

카메라 영상에서 불꽃과 연기를 탐지하는 과정을 공부한 2022년 프로젝트입니다. 데이터 라벨 정리와 학습 실험, YOLOv5 ONNX 모델을 OpenCV DNN으로 실행하는 코드를 모아두었습니다.

## 남겨둔 코드

| 경로 | 내용 |
| --- | --- |
| [fire_code/](fire_code/) | 라벨 변환, 데이터 분할·샘플링, YOLOv5 학습·탐지 노트북 |
| [fire_code/yolov5_dnn.py](fire_code/yolov5_dnn.py) | 카메라 입력, ONNX 추론, NMS 후처리, 탐지 상자 표시와 음성 알림 |
| [Object_detection_file/](Object_detection_file/) | ONNX 모델, 클래스 목록, 추론 코드 사본 |

당시 작업 기록에는 모델 경량화, Jetson 연결, OpenCV 카메라 연결을 진행한 내용이 남아 있습니다. 이 저장소에는 탐지 코드와 노트북이 중심으로 정리돼 있으며, 주행 제어나 로봇 전체 실행 절차는 포함돼 있지 않습니다.

## 실행 전에

오래된 실험 환경의 경로가 코드에 남아 있습니다. 그대로 실행하기보다 아래 항목을 먼저 확인해주세요.

1. `yolov5_dnn.py`의 `classesFile`과 `modelWeights`를 현재 파일 위치에 맞춥니다.
2. 클래스 목록의 순서와 개수가 사용할 ONNX 모델의 출력과 일치하는지 확인합니다.
3. 카메라 번호와 `cv2.imshow`를 사용할 수 있는 환경을 확인합니다.

추론 코드에 필요한 패키지는 `opencv-python`, `numpy`, `pyttsx3`입니다. 음성 출력에는 운영체제의 음성 엔진도 필요합니다.

```bash
python -m pip install opencv-python numpy pyttsx3
python fire_code/yolov5_dnn.py
```

학습 노트북은 데이터와 당시 YOLO 환경을 별도로 준비해야 합니다. 원본 데이터는 저장소에 포함하지 않았고, 의존성 버전도 고정돼 있지 않습니다.

## 데이터와 참고 자료

- [AI Hub 열화상 카메라 이미지](https://aihub.or.kr/aidata/27710)
- [AI Hub 화재 발생 예측 영상](https://aihub.or.kr/aidata/34121)
- [YOLOv5 학습 참고 글](https://developeryoung.tistory.com/15?category=879762)
- [초기 조사에 참고한 YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)

불꽃·연기뿐 아니라 구름, 안개, 조명 등 혼동하기 쉬운 장면도 함께 살펴봤습니다. 데이터 이용 조건은 각 배포처에서 확인해야 합니다.

## 당시 기록

- 2022-05-16: 학습 데이터를 라벨별로 분류
- 2022-07-20: YOLO 학습 진행

![당시 탐지 예시](https://user-images.githubusercontent.com/80506107/178093700-1019e16f-6e80-428b-b2ba-923bbe480ee3.png)

현재 README에는 별도로 검증한 탐지 성능 수치를 적지 않았습니다. 다음에 다시 정리한다면 실행 환경과 클래스 구성을 먼저 맞추고, 오탐 사례와 추론 시간을 같은 조건에서 측정해보고 싶습니다.
