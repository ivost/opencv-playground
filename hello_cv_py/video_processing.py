import cv2
# import numpy as np
# import dlib
# python -m pip install opencv-contrib-python
# doesn't work

capture = cv2.VideoCapture("./video/lemon.mp4")
if not capture.isOpened():
    print("Could not open video!")
    exit(4)

cv2.namedWindow("Input Video", cv2.WINDOW_NORMAL)
cv2.namedWindow("Output Video", cv2.WINDOW_NORMAL)
cv2.namedWindow("Hue", cv2.WINDOW_NORMAL)

while True:
    # capture frame
    ret, frame = capture.read()

    if not ret:
        break

    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Obtain Hue channel
    h = hsv[:, :, 0]

    # Apply thresholding
    hCopy = h.copy()
    h[hCopy > 40] = 0
    h[hCopy <= 40] = 1

    # Display frame
    cv2.imshow("Input Video", frame)
    cv2.imshow("Output Video", frame * h[:, :, np.newaxis])
    cv2.imshow("Hue", h * 255)

    k = cv2.waitKey(10)
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
