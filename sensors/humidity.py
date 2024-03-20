from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_humidity_v2 import BrickletHumidityV2

# Replace with the UID of your RGB LED Button Bricklet
UID_LED_BTN = "HFy"

# Keep as is, unless you changed the port in the Tinkerforge software
HOST = "localhost"
PORT = 4223

ipcon = IPConnection()
ipcon.connect(HOST, PORT)

def cb_humidity(humidity):
    print(f"Relative Humidity: {humidity/100.0:.2f} %")

sensor = BrickletHumidityV2(UID_LED_BTN, ipcon)
sensor.register_callback(sensor.CALLBACK_HUMIDITY, cb_humidity)
sensor.set_humidity_callback_configuration(1000, False, 'x', 0, 0)

input("Press key to exit\n")

ipcon.disconnect()