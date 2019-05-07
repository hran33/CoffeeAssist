import sys
import I2C_LCD_driver
import time

# Set up LCD
mylcd = I2C_LCD_driver.lcd()

# Set up HX711 module
EMULATE_HX711=False

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(379)
hx.reset()
hx.tare()

# Set up Micro:bit
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)

# Get weight value and display on LCD display
def showweight():
    global val
    val = hx.get_weight(5)
    mylcd.lcd_display_string("W:"+str(val)+"g",2)

# Reset timer
def cleartimer():
    mylcd.lcd_display_string(" "*8,2,8)
    mylcd.lcd_display_string("T:"+str(0)+"s",2,8)
    
# Reset load cell sensor
def resetW():
    hx.reset()
    hx.tare()
   
# Display instruction
def instruct():
    mylcd.lcd_display_string("Button A: Weigh", 1)
    mylcd.lcd_display_string("button B: Brew", 2)
    time.sleep(2)
    mylcd.lcd_clear()

# Exit program and clear lcd display
def cleanAndExit():
    if not EMULATE_HX711:
        GPIO.cleanup()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Bye!")
    sys.exit()

# Countdown timer for t seconds
def timer(t):
    mylcd.lcd_display_string(" "*16,1)
    mylcd.lcd_display_string("Brewing",1)
    for i in range (t,-1,-1):
        mylcd.lcd_display_string("T:"+str(i)+"s",2,8)
        time.sleep(1)
        if i == -1:
            break

# Set conditional variables
flag = 0
inst = 0

while True:
    try:
        # Show the instruction when program starts
        while inst == 0:
            instruct()
            break
        inst = inst + 1
        # Wait for mode selection
        while inst == 1:
            # Button A: Weighing mode
            if GPIO.input(27):
                mylcd.lcd_display_string("Weighing",1)
                showweight()
            # Button B: Brewing mode
            if GPIO.input(17):
                resetW()
                # First pour
                while flag == 0:
                    mylcd.lcd_display_string("Add water to 60",1)
                    showweight()
                    if val >= 60 :
                        timer(30)
                        cleartimer()
                        flag = flag + 1
                # Second pour
                while flag == 1:
                    mylcd.lcd_display_string("Add water to 150",1)
                    showweight()
                    if val >= 150:
                        timer(20)
                        cleartimer()
                        flag = flag + 1
                # Third pour
                while flag == 2: 
                    mylcd.lcd_display_string("Add water to 250",1)
                    showweight()
                    if val >= 250:
                        timer(20) 
                        cleartimer()
                        flag = flag + 1
                # Fourth pour
                while flag == 3: 
                    mylcd.lcd_display_string("Add water to 350",1)
                    showweight()
                    if val >= 350:
                        timer(20)
                        cleartimer()
                        flag = flag + 1
                # Brewing completed
                mylcd.lcd_clear()
                mylcd.lcd_display_string("Enjoy your",1)
                mylcd.lcd_display_string("coffee!",2)
                time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
