# Face-detection-MTCNN
Detect Faces in images and live webcam feed

## Introduction
MTCNN (Multi-task Cascaded Convolutional Neural Networks) is an algorithm consisting of 3 stages, which detects the bounding boxes of faces in an image along with their 5 Point Face Landmarks. Each stage gradually improves the detection results by passing it’s inputs through a CNN, which returns candidate bounding boxes with their scores, followed by non max suppression.


## Working
This is an implementation of MTCNN. MTCNN gives 5 keypoints in a face, using those 5 keypoints, this code generates 4 more keypoints. It can detect multiple faces in an image or in live webcam feed. 

## Libraries
* opencv _ _ _ _ _ _ 4.1
* tensorflow _ _ _ _ 1.14
* numpy _ _ _ _ _ _ 1.16
* os
* mtcnn

## Sample Images



<img src="https://github.com/aashishrai3799/Face-detection-MTCNN/blob/master/sample_images/input_3.jpg" width="480">
<img src="https://github.com/aashishrai3799/Face-detection-MTCNN/blob/master/sample_images/input_2.jpg" width="480">
<img src="https://github.com/aashishrai3799/Face-detection-MTCNN/blob/master/sample_images/input_4.jpg" width="480">
<img src="https://github.com/aashishrai3799/Face-detection-MTCNN/blob/master/sample_images/input_1.jpg" width="480">



