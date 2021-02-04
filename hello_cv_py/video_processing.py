import time

# https://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/

import cv2
import numpy as np

from stats import Stats

threshold = 40
sx = 10
sy = 50

# 10X smaller
ww = 384
wh = 216

INP = "input"
OUT = "output"

hidden = True
hidden = False

use_cam = True

if use_cam:
    capture = cv2.VideoCapture(0)
else:
    capture = cv2.VideoCapture("./video/lemon.mp4")

if not capture.isOpened():
    print("Could not open video!")
    exit(4)

print("Press ESC to exit")

flags = cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO

cv2.namedWindow(OUT, flags)
cv2.resizeWindow(OUT, ww, wh)
cv2.moveWindow(OUT, sy + ww, sx)

cv2.namedWindow(INP, flags)
cv2.resizeWindow(INP, ww, wh)
cv2.moveWindow(INP, sy, sx)

s = Stats()
s.begin()
while True:
    s.mark()
    ret, frame = capture.read()
    if not ret:
        break
    s.bump()
    if not hidden:
        # print(f"frame size {frame.shape}")
        frame = cv2.resize(frame, (ww, wh))
        # print(f"resized {frame.shape}")
        cv2.imshow(INP, frame)
        # print(f"after imshow {frm.shape}")

        # # Convert frame to HSV
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Obtain Hue channel
        hue = frame[:, :, 0]
        # Apply thresholding
        hCopy = hue.copy()
        hue[hCopy > threshold] = 0
        hue[hCopy <= threshold] = 1
        # # increase the dimension of the existing array by one more dimension, when used once
        frame = frame * hue[:, :, np.newaxis]
        cv2.imshow(OUT, frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

s.end()
print(s.fps_summary())

capture.release()
cv2.destroyWindow(INP)
cv2.destroyWindow(OUT)
cv2.destroyAllWindows()

exit(0)
