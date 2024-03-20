from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_button import BrickletRGBLEDButton
import time


# Replace with the UID of your RGB LED Button Bricklet
UID_LED_BTN = "DnY"

# Keep as is, unless you changed the port in the Tinkerforge software
HOST = "localhost"
PORT = 4223

ipcon = IPConnection()
ipcon.connect(HOST, PORT)

btn = BrickletRGBLEDButton(UID_LED_BTN, ipcon)

# Set the color of the button's LED
btn.set_color(255, 0, 0)

input("Hit enter to start the color changing loop")
print("The button's color will change every second from red to green to blue. The cycle repeats 3 times.")

c = 0
while c < 3:
    c = c +1
    print(f"Cycle {c}/3")
    btn.set_color(255, 0, 0)
    time.sleep(1)
    btn.set_color(0, 255, 0)
    time.sleep(1)
    btn.set_color(0, 0, 255)
    time.sleep(1)

ipcon.disconnect()