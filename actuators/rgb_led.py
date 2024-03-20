from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2
import random

# Replace with the UID of your RGB LED Button Bricklet
UID_LED_BTN = "ZDW"

# Keep as is, unless you changed the port in the Tinkerforge software
HOST = "localhost"
PORT = 4223

ipcon = IPConnection()
ipcon.connect(HOST, PORT)

led = BrickletRGBLEDV2(UID_LED_BTN, ipcon)

# Set LED to red
led.set_rgb_value(255, 0, 0)

input("Hit enter to turn off the LED")

# Set the LED to black (off)
led.set_rgb_value(0, 0, 0)

# Choose a random color from red, green, blue
input("Hit enter to set the LED to a random color")

color = random.choice(["red", "green", "blue"])

if color == "red":
    print("Setting LED to red")
    led.set_rgb_value(255, 0, 0)
elif color == "green":
    print("Setting LED to green")
    led.set_rgb_value(0, 255, 0)
else:
    print("Setting LED to blue")
    led.set_rgb_value(0, 0, 255)

ipcon.disconnect()
