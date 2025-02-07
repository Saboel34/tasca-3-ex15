def on_gesture_shake():
    global NUM
    NUM = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

NUM = 0
NUM = 5

def on_forever():
    pass
basic.forever(on_forever)
