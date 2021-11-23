from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

tello.streamon()
# frame_read = tello.get_frame_read()
# cv2.imshow('tello stream', frame_read.frame)
# cv2.waitKeyEx()
while True:

    key=cv2.waitKeyEx(1)
    if key > -1:
        print('key : ', key)
    if key == ord('q'):
        break
    frame_read = tello.get_frame_read()

    cv2.imshow('tello stream', frame_read.frame)

 
tello.streamoff()
cv2.destroyAllWindows()

# tello.takeoff()

# tello.land()

 