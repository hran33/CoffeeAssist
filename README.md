# CoffeeAssist

This is a Raspberry Pi Pour-over coffee making assistant that combines the function of a kitchen scale and a countdown timer. The program is worte follwing the pour over drip coffee brewing guide.

<img src="https://github.com/hran33/CoffeeAssist/blob/master/setup.jpg">

# Supplies

You will need the following materals:
  - Raspberry Pi (tested on Pi 3)
  - Micro:bit
   - 16x2 I2C LCD Display and jumper wires (female-to-female)
  - Mini SD card (16GB minimum) with adapter, and a computer to use to image the initial SD card
  - Ethernet cable and wireless network credentials
  - Power supplies (for the most flexibility in adding future peripherals, an official 5V 2.5A power supply is recommended)
  - Load Cell Weight Sensor (0-5kg (0-11 lb) recommended)
  - HX711 Module
  
# Getting Started

Download and install the latest Raspbian Jessie Lite to your Pi's SD card.
Install the MU Editor by running ```sodu apt-get update && sudo apt-get install mu -y```

# Sensor & Display Hookups

## LCD Screen

* GND to Raspberry Pi pin 9 (GND)
* VCC to Raspberry Pi pin 2 (5V)
* SDA to Raspberry Pi pin 3 (GPIO2)
* SCL to Raspberry Pi pin 5 (GPIO3)

## HX711

* VCC to Raspberry Pi Pin 2 (5V)
* GND to Raspberry Pi Pin 6 (GND)
* DT to Raspberry Pi pin 29 (GPIO5) 
* SCK to Raspberry Pi Pin 31 (GPIO6)

## Micro:bit
* pin 0 to Raspberry Pi pin 11 (GPIO17)
* pin 1 to Raspberry Pi pin 13 (GPIO27)

# Setup

The completed program will preform the following functions: sense the weight on the scale and display the value on the lcd display, when reaches the pre-set value, timer starts counting diwn, when time's up, sense the weight again, repeat until program ends.

## Set up the hx711 module
First, we will set up the hx711 load cell library to read weight (from https://github.com/tatobari/hx711py
) by doing the following:
```
cd /home/pi/
git clone https://github.com/tatobari/hx711py
cd hx711
```
Next, import the library and set up the load cell to get values by putting the following at the beginning:
```
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
```
Change the reference unit accordingly to calibrate

## Set up the LCD Screen
To enable the LCD screen, follow [these instructions](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/), make sure to include the library at the beginning of the code:
```
import I2C_LCD_driver
```
```
mylcd = I2C_LCD_driver.lcd()
```

## Set up the micro:bit

Set the micro:bit connection by importing:
```
import RPi.GPIO as GPIO
```
```
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
```
# General Notes
Button A on the microbit starts the kitchen scale mode with only the weighing funtion, button B starts the brewing mode. Put the coffee ware on the scale before starting the scale to avoid recuncant value readings. Change the time and weight for costumized routine. 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Circuit Basics](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/) - The lcd setup instruction
* [prattpi](https://github.com/prattpi/Raspberry-Pi-Datalogger/blob/master/README.md) - lcd connection
* [tatobari](https://github.com/tatobari/hx711py) - HX711 connection
