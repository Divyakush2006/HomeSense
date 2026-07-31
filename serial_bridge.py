"""Serial transport between the assistant and the Arduino controller.

Commands are single-byte opcodes; the switch in
firmware/homesense_controller/homesense_controller.ino must stay in sync.
"""

import os
import time

import serial

PORT = os.getenv("HOMESENSE_SERIAL_PORT", "COM10")
BAUDRATE = int(os.getenv("HOMESENSE_BAUDRATE", "9600"))

arduino = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=0.1)


def write_read(x):
    x = str(x)
    arduino.write(bytes(x, "utf-8"))
    time.sleep(0.05)


def control(value):
    write_read(value)
