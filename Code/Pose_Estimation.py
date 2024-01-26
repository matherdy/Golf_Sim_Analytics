"""
Following the video https://www.youtube.com/watch?v=brwgBf6VB0I&t=609s on human pose estimation
using cv2 (openCV) and mediapipe
"""


import time

import cv2
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
# https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
# This link is a reference guide for where each landmark is

pose = mpPose.Pose()

vid_path = r"/Users/dylanmather/Documents/Projects/Golf_Sim/Golf_Sim_Analytics/Sample_Vids/Dylan_Swing_Bandon.MOV"

cap = cv2.VideoCapture(vid_path)
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    # print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)

            # calculate the pixle values by multiplying the lm.x and lm.y image ratio by w and h
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)

    cv2.waitKey(1)
