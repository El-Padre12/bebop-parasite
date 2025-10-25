#!/usr/bin/python3
import serial_util
import songs

from pyPS4Controller.controller import Controller


class MyController(Controller):
    playlist = songs.SongManager()

    alog_up = 0
    alog_dn = 0
    alog_ri = 0
    alog_le = 0

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L1_press(self):
        self.playlist.songLeft()

    def on_R1_press(self):
        self.playlist.songRight()

    # Brushes
    #   def on_R3_right(self, value):
    #        serial_util.send_as_bytes(b'\x8a\x01')

    # Motor
    #   def on_R3_down(self, value):
    #        serial_util.send_as_bytes(b'\x8a\x02')

    def on_circle_press(self):  # up
        serial_util.send_as_bytes(b'\x89\xFE\x0C\x00\x00')

    def on_square_press(self):  # down
        serial_util.send_as_bytes(b'\x89\x01\xF4\x00\x00')

    def on_triangle_press(self):  # left
        serial_util.send_as_bytes(b'\x89\xD8\xF0\x00\x01')

    def on_x_press(self):  # right
        serial_util.send_as_bytes(b'\x89\x27\x10\x00\x01')

    def on_share_press(self):
        self.playlist.play_current_song()

    def on_circle_release(self):
        serial_util.send_as_bytes(b'\x89\x00\x00\x00\x00')

    def on_triangle_release(self):
        serial_util.send_as_bytes(b'\x89\x00\x00\x00\x00')

    def on_x_release(self):
        serial_util.send_as_bytes(b'\x89\x00\x00\x00\x00')

    def on_square_release(self):
        serial_util.send_as_bytes(b'\x89\x00\x00\x00\x00')

    def on_options_press(self):
        serial_util.send_as_bytes(b'\x85')

    def on_options_release(self):
        # reset sequence that works half the time
        # passive
        serial_util.send_as_bytes(b'\x80')
        # safe mode
        serial_util.send_as_bytes(b'\x82')
        # full control
        serial_util.send_as_bytes(b'\x84')

    def on_L3_release(self):
        self.alog_le = 0
        self.alog_ri = 0
        self.alog_dn = 0
        self.alog_up = 0

        serial_util.send_as_bytes(b'\x89\x00\x00\x00\x00')

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
        serial_util.send_as_bytes(bytestringBuilder)

# L analog - translate coords to 8 bit vals (pos and neg) (omnidirectional)
# -32000 - 32000

# Start - Programmatically play roomba notes

def main():

    # passive
    serial_util.send_as_bytes(b'\x80')

    # safe mode
    serial_util.send_as_bytes(b'\x82')

    # full control
    serial_util.send_as_bytes(b'\x84')

    # serial_util.send_as_bytes(b'\x8c\x00')
    controller = MyController(interface="/dev/input/js0",connecting_using_ds4drv=False)
    controller.listen(400)


if __name__ == "__main__":
    main()
