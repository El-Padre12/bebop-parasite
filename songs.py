import enum
import serial_util
import time


class SongManager():

    songAmount = 1
    currentSong = 0

    def songLeft(self):
        self.currentSong = abs((self.currentSong - 1) % self.songAmount)

    def songRight(self):
        self.currentSong = abs((self.currentSong + 1) % self.songAmount)

    def play_current_song(self):
        if (self.currentSong == 0):
            # play a single note and sleep 0.1
            self.la_cucaracha()

    def la_cucaracha(self):
        # First song section
        serial_util.send_as_bytes(b'\x8C\x00\x0F\x37\x10\x37\x10\x37\x10\x3c\x1A\x40\x1A\x37\x10\x37\x10\x37\x10\x3c\x1A\x40\x1A\x3c\x10\x3c\x10\x3b\x10\x3b\x10\x39\x10\x39\x10\x37\x1A')

        # Second song section
        serial_util.send_as_bytes(b'\x8C\x01\x02\x39\x10\x37\x1A')

        serial_util.send_as_bytes(b'\x8d\x00')
        #serial_util.send_as_bytes(b'\x8d\x00')

        time.sleep(4.48)
        print("FuckOff")

        serial_util.send_as_bytes(b'\x8d\x01')
