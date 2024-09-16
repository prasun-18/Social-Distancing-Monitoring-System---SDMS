# Social-Distance-Monitoring-in-Real-Time

Access the publication here: (https://lnkd.in/gScQW75u)
Social distancing in Real-Time using live video stream/IP camera in OpenCV.

> This is an improvement/modification to (https://www.pyimagesearch.com/2020/06/01/opencv-social-distancing-detector/).

---
### Use case: 
- counting the number of people in the stores/buildings/shopping malls etc., in real-time.
- It can also be implemented in the exam hall when invigilator is busy during answer sheet check-up.
- Sending an alert to the staff if the people are way over the social distancing limits.
- Optimizing the real-time stream for better performance (with threading).
- Acts as a tackle measure in mediacl feild for diseases such as COVID-19, Ebola, Tuberculosis (TB).
- Acts as a tackle measure during time of curfew.

---
## Proposed System
Our approach uses artificial intelligence tools such as deep learning and computer vision to track people in different environments and measure adherence to social distancing guidelines and can give notifications each time social distancing rules are violated also known as Smart Distancing. We have built a Machine Learning based model which utilizes OpenCV computer vision framework to monitor if the social distancing is being maintained by the persons detected in the frame. There are three level of detection red, yellow and green. When persons are maintaining minimum physical distancing then the detected boxes are green indicating that its safe. When the persons are getting closer to the minimum distance to be maintained then it turns yellow, finally the boxes turn red if the persons are violating the minimum physical distancing. The project is dynamic and can be customized to run on a variety of inputs, it can take any video as input file, it can take input from the webcam of the laptop and also it can take input from a CCTV camera using its IP address and produce the real time output. The project also sends an alert email and rings an alarm bell when the violations exceed a certain threshold. The project produces output with high accuracy while still leaving some room for future developments.

---
## Hardware Requirement

| Component       | Specification                         |
|-----------------|---------------------------------------|
| Processor       | Any Processor above 500MHz, preferably an Intel Core i7 7th Gen |
| RAM             | 8GB                                   |
| Hard Disk       | 50GB, preferably an SSD               |
| Input Device    | Standard Keyboard, Mouse, and Camera  |
| Output Device   | VGA and High-Resolution Monitor        |
| Internet        | Internet connection is required to send email alerts |

---
## Software Requirement

| Component          | Specification                                                      |
|--------------------|--------------------------------------------------------------------|
| Operating System   | Windows 10                                                         |
| IDE                | Any Python IDE with installed libraries                            |
| Python             | Python 3                                                           |
| Python Libraries   | OpenCV, Scikit-learn, NumPy, Argparse, Imutils, Winsound, Smtplib, SSL, OS, Time |



---
## Table of Contents
* [Simple Theory](#simple-theory)
* [Running Inference](#running-inference)
* [Features](#features)
* [References](#references)

## Simple Theory
**Object detection:**
- We will be using YOLOv3, trained on COCO dataset for object detection.
- In general, single-stage detectors like YOLO tend to be less accurate than two-stage detectors (R-CNN) but are significantly faster.
- YOLO treats object detection as a regression problem, taking a given input image and simultaneously learning bounding box coordinates and corresponding class label probabilities.
- It is used to return the person prediction probability, bounding box coordinates for the detection, and the centroid of the person.

---
**Distance calculation:**
- NMS (Non-maxima suppression) is also used to reduce overlapping bounding boxes to only a single bounding box, thus representing the true detection of the object. Having overlapping boxes is not exactly practical and ideal, especially if we need to count the number of objects in an image.
- Euclidean distance is then computed between all pairs of the returned centroids. Simply, a centroid is the center of a bounding box.
- Based on these pairwise distances, we check to see if any two people are less than/close to 'N' pixels apart.

## Running Inference
- Install all the required Python dependencies:
```
  pip install imutils scipy numpy opencv-python

```
- If you would like to use GPU, set ```USE_GPU = True``` in the config. options at 'mylib/config.py'.

- Note that you need to build OpenCV with CUDA (for an NVIDIA GPU) support first:

- To run inference on a test video file, head into the directory/use the command:
```
python run.py -i (address of video files) mylib/videos/test.mp4
```
- To run inference on an IP camera, Setup your camera url in 'mylib/config.py':


- Enter the ip camera url
```(e.g., url = 'http://191.178.0.100:8040/video') # Change with your IP address of camera/IP cam app of the phone```
-url = ''

- Then run with the command:
```
python run.py
```

- Set url = 0 for webcam.

---

### Features
The following are examples of the added features. Note: You can easily on/off them in the config. options (mylib/config.py):

---
### 1. Real-Time alert:
- If selected, we send an email alert in real-time. Use case: If the total number of violations (say 10 or 30) exceeded in a store/building, we simply alert the staff.
- You can set the max. violations limit in config (```Threshold = 15```).
- This is pretty useful considering the COVID-19 scenario.

---
### Note: To setup the sender email, please refer the instructions inside 'mylib/mailer.py'. Setup receiver email in the config.

---
### 2. Threading:
- Multi-Threading is implemented in 'mylib/thread.py'. If you ever see a lag/delay in your real-time stream, consider using it.
- Threading removes OpenCV's internal buffer (which basically stores the new frames yet to be processed until your system processes the old frames) and thus reduces the lag/increases fps.
- If your system is not capable of simultaneously processing and outputting the result, you might see a delay in the stream. This is where threading comes into action.
- It is most suitable for solid performance on complex real-time applications. To use threading:

---
set ```Thread = True``` in the config.

---
### 3. People counter:
- If enabled, we simply count the total number of people: set ```People_Counter = True``` in the config.

---
### 4. Desired violations limits:
- You can also set your desired minimum and maximum violations limits. For example, ```MAX_DISTANCE = 80``` implies the maximum distance 2 people can be closer together is 80 pixels. If they fell under 80, we treat it as an 'abnormal' violation (yellow).
- Similarly ```MIN_DISTANCE = 50``` implies the minimum distance between 2 people. If they fell under 50 px (which is closer than 80), we treat it as a more 'serious' violation (red).
- Anything above 80 px is considered as a safe distance and thus, 'no' violation (green).

---
## References
***Main:***
- YOLOv3 paper: https://arxiv.org/pdf/1804.02767.pdf
- YOLO original paper: https://arxiv.org/abs/1506.02640
- YOLO TensorFlow implementation (darkflow): https://github.com/thtrieu/darkflow

---
### Optional:
- More theory: https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/
- Other trained model weights from official doc: https://pjreddie.com/darknet/yolo/

---
### Thanks for the reading & have fun!

