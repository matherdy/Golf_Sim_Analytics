"""
Following the video https://www.youtube.com/watch?v=brwgBf6VB0I&t=609s on human pose estimation
using cv2 (openCV) and mediapipe
"""


import time

import cv2
import mediapipe as mp


class poseDetector:
    def __init__(
        self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5
    ):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        # https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
        # This link is a reference guide for where each landmark is

        self.pose = self.mpPose.Pose(
            self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon
        )

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)

        if results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(
                    img, results.pose_landmarks, self.mpPose.POSE_CONNECTION
                )

            # for id, lm in enumerate(results.pose_landmarks.landmark):
            #     h, w, c = img.shape
            #     print(id, lm)

            #     cx, cy = int(lm.x * w), int(lm.y * h)
            #     cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return img


def main():
    cap = cv2.VideoCapture("Sample_Vids/Dylan_Swing_Bandon.MOV")
    pTime = 0

    detector = poseDetector()
    while True:
        success, img = cap.read()
        detector.findPose(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(
            img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3
        )
        cv2.imshow("Image", img)

        cv2.waitKey(1)


if __name__ == "__main__":
    main()
