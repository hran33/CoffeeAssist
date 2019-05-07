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

<img src="https://github.com/hran33/CoffeeAssist/blob/master/CoffeeAssistFritzing.jpg">

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
Follow [these instructions](https://github.com/tatobari/hx711py) to assamble the load cell and hx711 amplifier 
)
Change the reference unit accordingly to calibrate
```
hx.set_reference_unit(379)
```

## Set up the LCD Screen
To enable the LCD screen, follow [these instructions](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)

## Set up the microcontroller
Open the control.py file in MU Editor and flash it to the micro:bit

# General Notes

Button A on the microbit starts the kitchen scale mode with only the weighing funtion, button B starts the brewing mode. Put the coffee ware on the scale before starting the scale to avoid recuncant value readings. Change the timer value and weight for costumized routine. 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Circuit Basics](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/) - The lcd setup instruction
* [prattpi](https://github.com/prattpi/Raspberry-Pi-Datalogger/blob/master/README.md) - lcd connection
* [tatobari](https://github.com/tatobari/hx711py) - HX711 connection
