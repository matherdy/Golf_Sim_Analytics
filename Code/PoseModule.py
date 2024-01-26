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
        self.results = None

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        # https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
        # This link is a reference guide for where each landmark is
        # print(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)
        self.pose = self.mpPose.Pose(
            self.mode,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon,
        )

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(
                    img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS
                )
        return img

    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape

                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList


def main():
    # vid_path = r'/Users/dylanmather/Documents/Projects/Golf_Sim/Golf_Sim_Analytics/Sample_Vids/Dylan_Swing_Bandon.MOV'
    # vid_path = r"/Users/dylanmather/Documents/Projects/Golf_Sim/Golf_Sim_Analytics/Sample_Vids/swing_1.MOV"
    vid_path = r"/Users/dylanmather/Documents/Projects/Golf_Sim/Golf_Sim_Analytics/Sample_Vids/swing_2.MOV"
    cap = cv2.VideoCapture(vid_path)
    pTime = 0
    detector = poseDetector(mode=False)
    limb_number = 26
    while True:

        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        print(lmList[limb_number])
        cv2.circle(
            img,
            (lmList[limb_number][1], lmList[limb_number][2]),
            5,
            (255, 0, 0),
            cv2.FILLED,
        )
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
