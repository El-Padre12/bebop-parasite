#!/usr/bin/python3
import time

from pyPS4Controller.controller import Controller
import serial

ser = serial.Serial(port='/dev/irobot', baudrate=57600)

class MyController(Controller):
    alog_up = 0
    alog_dn = 0
    alog_ri = 0
    alog_le = 0

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    def on_L1_press(self):
        print("Selecting one song left")
        
    def on_R1_press(self):
        print("Selecting one song right")

    # Brushes
    #   def on_R3_right(self, value):
    #        send_as_bytes(b'\x8a\x01', ser)

    # Motor
    #   def on_R3_down(self, value):
    #        send_as_bytes(b'\x8a\x02', ser)

    def on_circle_press(self):  # up
        send_as_bytes(b'\x89\xFE\x0C\x00\x00', ser)

    def on_square_press(self):  # down
        send_as_bytes(b'\x89\x01\xF4\x00\x00', ser)

    def on_triangle_press(self):  # left
        send_as_bytes(b'\x89\xD8\xF0\x00\x01', ser)

    def on_x_press(self):  # right
        send_as_bytes(b'\x89\x27\x10\x00\x01', ser)


    def on_share_press(self):
        play_la_cucaracha(ser)

    def on_playstation_button_press(self):
        play_la_cucaracha(ser)

    def on_circle_release(self):
        send_as_bytes(b'\x89\x00\x00\x00\x00', ser)

    def on_triangle_release(self):
        send_as_bytes(b'\x89\x00\x00\x00\x00', ser)

    def on_x_release(self):
        send_as_bytes(b'\x89\x00\x00\x00\x00', ser)

    def on_square_release(self):
        send_as_bytes(b'\x89\x00\x00\x00\x00', ser)

    def on_options_press(self):
        send_as_bytes(b'\x85', ser)

    def on_options_release(self):
        # reset sequence that works half the time
        # passive
        send_as_bytes(b'\x80', ser)
        # safe mode
        send_as_bytes(b'\x82', ser)
        # full control
        send_as_bytes(b'\x84', ser)

    def on_L3_release(self):
        self.alog_le = 0
        self.alog_ri = 0
        self.alog_dn = 0
        self.alog_up = 0

        send_as_bytes(b'\x89\x00\x00\x00\x00', ser)

    def on_L3_x_at_rest(self):
        self.alog_le = 0
        self.log_ri = 0

    def on_L3_y_at_rest(self):
        self.alog_up = 0
        self.alog_dn = 0

    def on_L3_left(self, value):
        left = int(value / 65)
        self.alog_le = left
        self.alog_ri = 0
        self.update_and_send()

    def on_L3_right(self, value):
        right = int(value / 65)
        self.alog_ri = right
        self.alog_le = 0
        self.update_and_send()

    def on_L3_up(self, value):
        up = int(value / 65)
        self.alog_up = up
        self.update_and_send()

    def on_L3_down(self, value):
        dn = int(value / 65)
        self.alog_dn = dn
        self.update_and_send()

    def update_and_send(self):
        bytestringBuilder = bytearray(b'\x89')
        chnk1 = -(self.alog_up + self.alog_dn)
        chnk2 = -(self.alog_le + self.alog_ri)

        bytestringBuilder += chnk1.to_bytes(2, byteorder='big', signed=True)
        bytestringBuilder += chnk2.to_bytes(2, byteorder='big', signed=True)
        send_as_bytes(bytestringBuilder, ser)

# L analog - translate coords to 8 bit vals (pos and neg) (omnidirectional)
# -32000 - 32000

# Start - Programmatically play roomba notes

def send_as_bytes(bytes, port):
    port.write(bytes)

def play_la_cucaracha(port):
    send_as_bytes(b'\x8C\x00\x0F\x37\x10\x37\x10\x37\x10\x3c\x1A\x40\x1A\x37\x10\x37\x10\x37\x10\x3c\x1A\x40\x1A\x3c\x10\x3c\x10\x3b\x10\x3b\x10\x39\x10\x39\x10\x37\x1A', ser)
    send_as_bytes(b'\x8C\x01\x02\x39\x10\x37\x1A', ser)

    send_as_bytes(b'\x8d\x00', ser)
    # send_as_bytes(b'\x8d\x00', ser)

    time.sleep(4.48)
    print("FuckOff")

    send_as_bytes(b'\x8d\x01', ser)

def main():

    # passive
    send_as_bytes(b'\x80', ser)
    # safe mode
    send_as_bytes(b'\x82', ser)
    # full control
    send_as_bytes(b'\x84', ser)

    # send_as_bytes(b'\x8c\x00', ser)

    controller = MyController(interface="/dev/input/js0",
                              connecting_using_ds4drv=False)
    controller.listen(400)

if __name__ == "__main__":
    main()
