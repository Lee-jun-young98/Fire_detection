# Fire_detection
# 화재 감지 로봇

# 데이터셋
[열화상 카메라 이미지](https://aihub.or.kr/aidata/27710)

[화재 발생 예측 영상](https://aihub.or.kr/aidata/34121)

[https://github.com/Megvii-BaseDetection/YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)

- YOLOx를 통해 object detection

예시 사진)

![Untitled](https://user-images.githubusercontent.com/80506107/178093700-1019e16f-6e80-428b-b2ba-923bbe480ee3.png)


[화재 발생 예측 데이터셋 설명](%E1%84%92%E1%85%AA%E1%84%8C%E1%85%A2%20%E1%84%80%E1%85%A1%E1%86%B7%E1%84%8C%E1%85%B5%20%E1%84%85%E1%85%A9%E1%84%87%E1%85%A9%E1%86%BA%20f99237b1fca84f51b2adc053d300c0a5/Untitled.pdf)

## 데이터 설명

- label
    1. 검정색 연기
    2. 회색 연기
    3. 흰색 연기
    4. 화재(불꽃) 발생
    5. 구름
    6. 안개(연무)
    7. 조명
    8. 햇빛
    9. 흔들림이 있는 흰색/회색/검정색 물체(object)
    10. None
    
    1. 무관씬
    
![Untitled 1](https://user-images.githubusercontent.com/80506107/178093719-4241cf3f-89f6-43f3-aa66-906e1a759c8a.png)


# 논문

- [비디오 기반 딥러닝 융합 알고리즘에 의한 화재 감지 시스템에 관한 연구](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10605150)
    - CNN 기반 알고리즘, Alexnet 사용
    - accuracy는 97%, 음성 오탐 비율은 3.5%, 양성 오탐 비율은 2.4%
- [딥러닝기반 화재감지 시스템](https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE09371910)
- [S-FDS : 퍼지로직과 딥러닝 통합 기반의 스마트 화재감지 시스템](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07164790)
- [Convolutional Neural Network를 활용한 영상 기반의 화재 감지에 관한 연구](https://eds.s.ebscohost.com/eds/detail/detail?vid=4&sid=c030809a-2755-42b5-a7ac-94081b991abd%40redis&bdata=Jmxhbmc9a28mc2l0ZT1lZHMtbGl2ZQ%3d%3d#AN=edsker.000004392978&db=edsker)
- [화재 감지 시스템을 위한 다중 센서 데이터 퓨전 알고리즘의 구현](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09409711)
- [라즈베리파이 자율 주행 소방차](https://github.com/tpy7723/Self-Driving-Fire-Truck)
- [라즈베리파이 opencv 자율주행 소스 - Google Search](https://www.google.com/search?sxsrf=ALiCzsZnP7d8FSJB88BVD1dxPAEHQyVQqQ:1651475467671&q=%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4+opencv+%EC%9E%90%EC%9C%A8%EC%A3%BC%ED%96%89+%EC%86%8C%EC%8A%A4&sa=X&ved=2ahUKEwij--vEocD3AhUb82EKHSVlAjUQ1QJ6BAgfEAE&biw=1636&bih=935&dpr=1)
- [NVIDIA JETSON NANO 배터리 전압 문제 솔류션](http://daddynkidsmakers.blogspot.com/2019/12/nvidia-jetson-nano.html)

# 코드 참고
- [yolov5 를 customize해서 나만의 object detection 모델을 만들어보기](https://developeryoung.tistory.com/15?category=879762)

# 진행사항
2022-05-11 02, 07, 09 샘플 존재하지 않음
2022-05-16 Train 데이터 label별로 모두 나눔
2022-07-20 Yolo 데이터 학습

# 해야 할일

- [x]  로컬 설정하기
- [x]  Yolo 공부하기
- [x]  Yolo 클래스 분류하기
- [x]  Yolo 모델 경량화 하기
- [ ]  Jetson Yolo 모델 연결하기
- [ ]  opencv 카메라 연결해보기
