import cv2
from mtcnn.mtcnn import MTCNN
from draw_points import *
import os

print('Welcome to Face Detection \n\n Enter 1 to add image manually\n Enter 2 to detect face in Webcam feed')
n = int(input())
if n != 1 and n != 2:
    print('Wrong Choice')
    exit(0)

if n == 1:
    print('Enter complete address of the image')
    addr = str(input())
    if not os.path.exists(addr):
        print('Invalid Address')
        exit(0)

    print('Enter Resolution of output image (in heightXwidth format)')
    res = input().split('X')
    img = cv2.imread(addr)
    img = cv2.resize(img, (int(res[0]), int(res[1])))
elif n ==2:
    video_capture = cv2.VideoCapture(0)


detector = MTCNN()
ct = 0
alpha = 0.12
beta = 0.04

while True:

    if n == 2:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif n == 1:
        frame = img

    detect = detector.detect_faces(frame)

    if detect:

        boxes = detect[0]['box']
        keypoints = detect[0]['keypoints']
        show_points(frame, boxes, keypoints, alpha, beta)
        draw_lines(frame, boxes, keypoints, alpha, beta)


    # Display the resulting frame
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
video_capture.release()
cv2.destroyAllWindows()