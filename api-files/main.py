from imutils.object_detection import non_max_suppression 
import numpy as np 
import imutils 
import cv2 
import requests 
import time 
import argparse 

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def toNumpyVideo(toConvertAdress):
    cap = cv2.VideoCapture("media/demo_1.mp4")
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

    fc = 0
    ret = True

    while (fc < frameCount  and ret):
        ret, buf[fc] = cap.read()
        fc += 1

        cap.release()

    cv2.namedWindow('frame 10')
    cv2.imshow('frame 10', buf[9])

    cv2.waitKey(0)

video = 'media/demo_1.mp4'
print(video)
toNumpyVideo(video)
