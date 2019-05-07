from microbit import *
import time
pin1.write_digital(0)
pin0.write_digital(0)
while True:
    if button_a.was_pressed():
        display.show("W")
        pin1.write_digital(1)
        #time.sleep(10)
        #pin1.write_digital(0)
    if button_b.was_pressed():
        display.show("B")
        pin0.write_digital(1)
        #time.sleep(10)
        #pin0.write_digital(0)
    else:
        display.show(Image.SMILE)