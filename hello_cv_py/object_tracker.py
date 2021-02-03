import cv2
# import numpy as np
# import dlib
# python -m pip install opencv-contrib-python
# doesn't work

video = cv2.VideoCapture("./video/soccer.mp4")
if not video.isOpened():
    print("Could not open video!")
    exit(4)
# Read first frame
ret, frame = video.read()
# Check if frame read successfully
if not ret:
    print("Cannot read video")
    exit(4)
cv2.imshow("First Frame", frame)
cv2.waitKey(0)

# Specify the initial bounding box
bbox = cv2.selectROI(frame)
cv2.destroyAllWindows()
# Create tracker
# TLD Tracker
OpenCV_Tracker = cv2.TrackerTLD_create()
# Initialize OpenCV tracker
ret = OpenCV_Tracker.init(frame, bbox)

# Create a new window where we will display
# the results
cv2.namedWindow("Tracker")
# Display the first frame
cv2.imshow("Tracker", frame)

while True:
    # Read next frame
    ret, frame = video.read()

    # Check if frame was read
    if not ret:
        break

    # Update tracker
    found, bbox = OpenCV_Tracker.update(frame)

    # If object found, draw bbox
    if found:
        # Top left corner
        topLeft = (int(bbox[0]), int(bbox[1]))
        # Bottom right corner
        bottomRight = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        # Display bounding box
        cv2.rectangle(frame, topLeft, bottomRight, (0, 0, 255), 2)
    else:
        # Display status
        cv2.putText(frame, "Object not found", (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display frame
    cv2.imshow("Tracker", frame)
    k = cv2.waitKey(5)
    if k == 27:
        break

cv2.destroyAllWindows()
