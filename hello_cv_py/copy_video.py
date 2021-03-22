import time

import numpy as np
import cv2

video = "/home/ivo/Videos/airport-01.m4v"
cap = cv2.VideoCapture(video)

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps, "fps")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'MPEG')

size = (1920, 1080)
out = cv2.VideoWriter('/home/ivo/Videos/output.avi', fourcc, fps, size)

while cap.isOpened():
    now = time.time()
    ret, frame = cap.read()
    if not ret:
        print("read error")
        break
    # write the flipped frame
    out.write(frame)
    cv2.imshow('frame', frame)
    timeDiff = time.time() - now
    if timeDiff < 1.0 / fps:
        time.sleep(1.0 / fps - timeDiff)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
