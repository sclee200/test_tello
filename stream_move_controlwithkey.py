from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()
tello.streamon()

# img = cv2.imread('./flying-drone.jpg')
# cv2.imshow('flying drone',img) #keyboard input을 받기 위해
#keyboard control

def keyControl():
    key=cv2.waitKeyEx(1)
    if key > -1:
        print('key : ', key)
   
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

    return key
while True:

    key = keyControl()
    if key == ord('q'):
        break

    frame_read = tello.get_frame_read()
    cv2.imshow('tello stream', frame_read.frame)

tello.streamoff()
cv2.destroyAllWindows()