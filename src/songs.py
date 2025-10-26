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
        #serial_util.send_as_bytes(b'\x8c\x00\x01\x64\x10')
        #serial_util.send_as_bytes(b'\x8d\x00')   E       G       D       B       G       E       E 
        serial_util.send_as_bytes(b'\x8C\x00\x0e\x4c\x10\x4f\x10\x56\x1A\x53\x10\x4f\x10\x4c\x1A\x4c\x10\x4f\x10\x53\x1A\x4f\x10\x4a\x10\x47\x1A\x47\x10\x4a\x10\x4d\x1A')
    # G        B      G       D        B      B      D
        serial_util.send_as_bytes(b'\x8C\x01\x07\x4a\x10\x47\x10\x37\x1A\x4a\x1A\x40\x10\x41\x10\x37\x10') # song sec 2
        #                                         D     B        G       D
            
    # Play song sec 1
        serial_util.send_as_bytes(b'\x8d\x00')
        time.sleep(4.48)
        serial_util.send_as_bytes(b'\x8d\x01')
        
    # 2
    def mario(self):
        # 1st section
        serial_util.send_as_bytes
        (b'\x8c\x01\x0e\x4c\x0a\x4c\x0a\x4c\x0a\x48\x0a\x4c\x0a\x43\x0a\x43\x0a\x48\x0a\x43\x0a\x4c\x0a\x45\x0a\x47\x0a\x47\x0a')
        
        # 2nd section
        # serial_util.send_as_bytes
        # (b'\x8c\x01\x0e\x45\x0a\x43\x0a\x4c\x0a\x43\x0a\x45\x0a\x4d\x0a\x43\x0a\x4c\x0a\x48\x0a\x4a\x0a\x47\x0a')

        # first call
        serial_util.send_as_bytes(b'\x8d\x00')
  
        time.sleep(4.48)

        # second call
        # serial_util.send_as_bytes(b'\x8d\x01')

        # time.sleep(4.48)

        # #3rd call
        # serial_util.send_as_bytes(b'\x8d\x02')

        # time.sleep(4.48)

        # #4th call
        # serial_util.send_as_bytes(b'\x8d\x03')

        # #5th call
        # serial_util.send_as_bytes(b'\x8d\x04')

    # 3
    def tank(self):
        serial_util.send_as_bytes(b'\x8c\x00\x0E\x4c\x08\x4c\x08\x82\x04\x4c\x08\x4c\x08\x82\x04\x4c\x08\x4c\x08\x82\x04\x4c\x08\x4c\x08\x82\x04\x44\x08\x47\x08')
        serial_util.send_as_bytes(b'\x8d\x00')
        print("Playing tank!")
