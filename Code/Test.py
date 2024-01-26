import os
import time

import cv2
import PoseModule as pm

vid_dir = "//Users//dylanmather//Documents//Projects//Golf_Sim//Golf_Sim_Analytics//Sample_Vids//"
vid_paths = [vid_dir + path for path in os.listdir(vid_dir)]

vid_num = 5
limb_numbers = [20, 21, 24, 23]

vid_path = vid_paths[vid_num]

cap = cv2.VideoCapture(vid_path)
pTime = 0
detector = pm.poseDetector()


while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    for limb in limb_numbers:
        cv2.circle(img, (lmList[limb][1], lmList[limb][2]), 5, (255, 0, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Video processing stopped by user.")
        break


cap.release()
cv2.destroyAllWindows()
