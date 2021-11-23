from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()


img = cv2.imread('./flying-drone.jpg')
cv2.imshow('flying drone',img) #keyboard input을 받기 위해
#keyboard control
while True:

    key=cv2.waitKeyEx(1)
    if key > -1:
        print('key : ', key)
    if key == ord('q'):
        break
    # key = input('please input command')   

    if key ==ord("t"):
        tello.takeoff()
    if key ==ord("u"):
        tello.move_up(70)
    elif key == ord("f"):
        tello.move_forward(70)
    elif key == ord("b"):
        tello.move_back(70)
    elif key == ord("l"):
        tello.land()
    elif key == ord("c"):
        tello.rotate_clockwise(90)