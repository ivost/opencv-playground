# https://stackoverflow.com/questions/52068277/change-frame-rate-in-opencv-3-4-2
# https://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/

import time
from threading import Thread

import cv2
from imutils.video import FPS
import imutils


class MyCapture:
    def __init__(self, src=0):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return
            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()
            # todo: ensure reading at constant interval 1/fps sec
            time.sleep(1)
'''
frame_rate = 10
prev = 0

while capturing:

    time_elapsed = time.time() - prev
    res, image = cap.read()

    if time_elapsed > 1./frame_rate:
        prev = time.time()

        # Do something with your image here.
        process_image()
        
        
something like wait_for_frame 
        
'''



    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True


if __name__ == '__main__':

    hidden = False
    NUM_FRAMES = 300

    # created a *threaded* video stream, allow the camera sensor to warmup,
    # and start the FPS counter
    print("[INFO] sampling THREADED frames from webcam...")
    vs = MyCapture(src=0).start()
    fps = FPS().start()
    # loop over some frames...this time using the threaded stream
    while fps._numFrames < NUM_FRAMES:
        # grab the frame from the threaded video stream and resize it
        # to have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        if not hidden:
            cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
        # update the FPS counter
        fps.update()
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()
    exit(0)
