import cv2

# import numpy as np

# This code is taken from a tutorial from the openCV website about playing and taking
# video:  https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html


# This will take video from you camera and turn it to gray scale

# cap = cv2.VideoCapture(0)

# while(True):
#     #Capture frame by frame
#     ret,frame = cap.read()

#     #converts the video to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     #Display the frame
#     cv2.imshow("frame",gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# This will play a video from file

cap = cv2.VideoCapture("Sample_Vids/Dylan_Swing_Bandon.MOV")

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
