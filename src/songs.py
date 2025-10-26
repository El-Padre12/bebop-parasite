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
            self.mario()
        elif (self.currentSong == 3):
            self.tank()
        elif (self.currentSong == 4):
            self.mary_had_a_little_lamb()

    # 0

    def la_cucaracha(self):
        # First song section
        serial_util.send_as_bytes(b'\x8C\x00\x0F\x37\x10\x37\x10\x37\x10\x3c\x1A\x40\x1A\x37\x10\x37\x10\x37\x10\x3c\x1A\x40\x1A\x3c\x10\x3c\x10\x3b\x10\x3b\x10\x39\x10\x39\x10\x37\x1A')

        # Second song section
        serial_util.send_as_bytes(b'\x8C\x01\x01\x39\x1A')

        # Call first song
        serial_util.send_as_bytes(b'\x8d\x00')

        # Wait for first song to end
        time.sleep(4.48)

        # Call second song
        serial_util.send_as_bytes(b'\x8d\x01')

    # 1
    # Cats on Mars Attempt
    def cats_on_mars(self): #                    E       G       D110    B107    G       E
        serial_util.send_as_bytes(b'\x8c\x00\x0f\x4c\x10\x4f\x10\x56\x1A\x53\x10\x4f\x10\x4c\x1A\x4c\x10\x4f\x10\x53\x1A\x4f\x10\x4a\x10\x47\x1A\x47\x10\x4a\x10\x4d\x1A\x4d\x1A')
        serial_util.send_as_bytes(b'\x8c\x01\x07\x4a\x10\x47\x10\x43\x1A\x4a\x1A\x40\x1A\x41\x1A\x43\x1A') # song sec 2
        serial_util.send_as_bytes(b'\x8c\x02\x0e\x4c\x10\x4f\x10\x56\x1A\x53\x10\x4f\x10\x4c\x1A\x4c\x10\x4f\x10\x53\x1A\x4f\x10\x4a\x10\x47\x1A\x47\x10\x4a\x10')
        serial_util.send_as_bytes(b'\x8c\x03\x06\x4d\x1A\x4a\x10\x47\x10\x43\x1A\x4a\x1A\x43\x2A')

        serial_util.send_as_bytes(b'\x8d\x00')
        time.sleep(4.6)

        serial_util.send_as_bytes(b'\x8d\x01')
        time.sleep(2.6)

        serial_util.send_as_bytes(b'\x8d\x02')
        time.sleep(4.14)

        serial_util.send_as_bytes(b'\x8d\x03')

    # 2
    def mario(self):
        # 1st song
        serial_util.send_as_bytes(b'\x8c\x00\x02\x77\x18\x7c\x18')

        # call 1st song
        serial_util.send_as_bytes(b'\x8d\x00')
        serial_util.send_as_bytes(b'\x8d\x00')

        print("Playing Mario Coin Sound!")

    # 3
    def tank(self):
        serial_util.send_as_bytes(b'\x8c\x00\x0E\x4c\x08\x4c\x08\x82\x04\x4c\x08\x4c\x08\x82\x04\x4c\x08\x4c\x08\x82\x04\x4c\x08\x4c\x08\x82\x04\x44\x08\x47\x08')
        serial_util.send_as_bytes(b'\x8d\x00')
        print("Playing tank!")

    # 4
    def mary_had_a_little_lamb(self):
        #1st song
        serial_util.send_as_bytes(b'\x8c\x00\x0d\x4c\x18\x4a\x18\x48\x18\x4a\x18\x4c\x18\x4c\x18\x4c\x18\x4a\x18\x4a\x18\x4a\x18\x4c\x18\x43\x18\x43\x18')

        #call to 1st song
        serial_util.send_as_bytes(b'\x8d\x00')

        print("Playing 'Mary had a little lamb'")