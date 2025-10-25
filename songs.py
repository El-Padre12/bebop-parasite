import enum
import serial_util
import time

class SongManager():
    songAmount = 3
    currentSong = 0

    def songLeft(self):
        self.currentSong = abs((self.currentSong - 1) % self.songAmount)
        print(self.currentSong)

    def songRight(self):
        self.currentSong = abs((self.currentSong + 1) % self.songAmount)
        print(self.currentSong)

    def play_current_song(self):
        if (self.currentSong == 0):
            # play a single note and sleep 0.1
            self.la_cucaracha()
        elif (self.currentSong == 1):
            self.mario_death()

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

    #Cats on Mars Attempt
    def cats_on_mars(self): #                    E       G       D110    B107    G       E
        serial_util.send_as_bytes(b'\x8C\x00\x0F\x64\x10\x67\x10\x6e\x12\x6b\x10\x67\x10\x64\x12')
        serial_util.send_as_bytes(b'\x8d\x01')

    def mario_death(self):
        serial_util.send_as_bytes(b'\x8c\x00\x03\x3c\x3c\x84\x40\x3c\x40')
        serial_util.send_as_bytes(b'\x8d\x00')
    
    def tank(self):
        serial_util.send_as_bytes(b'\x8c\x00\x03\x73\x08\x73\x08\x73\x08')
        serial_util.send_as_bytes(b'\x8d\x00')
