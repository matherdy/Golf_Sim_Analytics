# import cv2
# import numpy as np

# #
# # https://www.youtube.com/watch?v=RaCwLrKuS1w

# videoCapture = cv2.VideoCapture(0)
# prevCircle = None
# dist = lambda x1, y1, x2, y2: (x1 - x2) ** 2 + (y1 - y2) ** 2

# while True:
#     ret, frame = videoCapture.read()

#     if not ret:
#         break

#     grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     blurFrame = cv2.GaussianBlur(grayFrame, (17, 17), 0)

#     circles = cv2.HoughCircles(
#         blurFrame,
#         cv2.HOUGH_GRADIENT,
#         1.2,
#         100,
#         param1=100,
#         param2=30,
#         minRadius=20,
#         maxRadius=100,
#     )

#     if circles is not None:
#         circles = np.uint16(np.around(circles))
#         chosen = None
#         for i in circles[0, :]:
#             if chosen is None:
#                 chosen = i
#             if prevCircle is not None:
#                 if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(
#                     i[0], i[1], prevCircle[0], prevCircle[1]
#                 ):
#                     chosen = i
#         cv2.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
#         cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
#         prevCircle = chosen

#     cv2.imshow("circles", frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# videoCapture.release()
# cv2.destroyAllWindows()


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

# cap = cv2.VideoCapture("Sample_Vids/Dylan_Swing_Bandon.MOV")

# while cap.isOpened():
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow("frame", gray)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()
