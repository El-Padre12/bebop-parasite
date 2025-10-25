import serial

ser = serial.Serial(port='/dev/irobot', baudrate=57600)


def send_as_bytes(bytes):
    ser.write(bytes)
