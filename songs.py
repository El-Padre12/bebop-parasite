import enum
import serial_util
import time

class SongManager():

    songAmount = 4
    currentSong = 0
    
    # TODO
    def initialize(self):
        serial_util.send_as_bytes(b'\x8C\x00\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    def songLeft(self):
        self.currentSong = abs((self.currentSong - 1) % self.songAmount)
        print(self.currentSong)

    def songRight(self):
        self.currentSong = abs((self.currentSong + 1) % self.songAmount)
        print(self.currentSong)

    def play_current_song(self):
        if (self.currentSong == 0):
            self.la_cucaracha()
        elif (self.currentSong == 1):
            self.cats_on_mars()
        elif (self.currentSong == 2):
            self.mario_death()
        elif (self.currentSong == 3):
            self.tank()

    # 0

    def la_cucaracha(self):
        # First song section
        serial_util.send_as_bytes(b'\x8C\x00\x0F\x37\x10\x37\x10\x37\x10\x3c\x1A\x40\x1A\x37\x10\x37\x10\x37\x10\x3c\x1A\x40\x1A\x3c\x10\x3c\x10\x3b\x10\x3b\x10\x39\x10\x39\x10\x37\x1A')

        # Second song section
        serial_util.send_as_bytes(b'\x8C\x01\x02\x39\x10\x37\x1A')

        # Call first song
        serial_util.send_as_bytes(b'\x8d\x00')

        # Wait for first song to end
        time.sleep(4.48)

        # Call second song
        serial_util.send_as_bytes(b'\x8d\x01')

    # 1

    # Cats on Mars Attempt
    def cats_on_mars(self): #                    E       G       D110    B107    G       E

        serial_util.send_as_bytes(b'\x8c\x00\x01\x64\x10')
        serial_util.send_as_bytes(b'\x8d\x00')

        serial_util.send_as_bytes(b'\x8C\x00\x06\x70\x67\x6e\x6b\x67\x70')
        serial_util.send_as_bytes(b'\x8d\x01')

    # 2
    def mario_death(self):
        serial_util.send_as_bytes(b'\x8c\x00\x06\x84\x20\x84\x20\x84\x20\x24\20\x84\x20\x2b\x20')
        #serial_util.send_as_bytes(b'\x8c\x00\x03\x3c\x3c\x84\x40\x3c\x40')
        serial_util.send_as_bytes(b'\x8d\x00')

    # 3
    def tank(self):
        serial_util.send_as_bytes(b'\x8c\x00\x03\x4c\x08\x4c\x08\x4c\x08')
        serial_util.send_as_bytes(b'\x8d\x00')
        print("Playing tank!")
