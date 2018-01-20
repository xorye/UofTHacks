import cv2
import numpy as np

# the video capture object (responsible for getting raw video data)
capture = cv2.VideoCapture(0)

while True:
    feed_on, frame = capture.read()
    #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ### Object detection below


    # Output the video feed
    cv2.imshow("Video Feed", frame)

    # Define how to exit and halt the video feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
