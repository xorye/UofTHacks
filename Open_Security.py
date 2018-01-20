import cv2
import numpy as np
import tweepy

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

'''
# Api keys required
CONSUMER_KEY ="VvPlmI6w4sdg3AdQ055nW0Mq6"
CONSUMER_SECRET = "vlGOr8mwZly5FWucbVvqDarbiVYMv8GIk2uEuHvYXaFuo8ZMyO"
ACCESS_KEY = "954725736790810627-0LIzKoQB26Ap4jgt3tS8Fiao3yZAjAM"
ACCESS_SECRET = "XPgIM9G0uNhGxzCMMoEm3qiplMOuwGt4f4iSobEIhsyCB"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Send a tweet
api.update_status("UofT Hack")
'''
