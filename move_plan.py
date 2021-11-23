from djitellopy import Tello

tello = Tello()
tello.connect()



while True:
    firstNumber = input('please input command')   

    if firstNumber == "0":
        tello.takeoff()
    if firstNumber == "1":
        tello.move_up(70)
    elif firstNumber == "2":
        tello.move_forward(70)
    elif firstNumber == "3":
        tello.move_back(70)
    elif firstNumber == "4":
        tello.land()
    elif firstNumber == "5":
        tello.rotate_clockwise(90)