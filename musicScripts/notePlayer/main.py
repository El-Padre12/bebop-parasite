import serial_util


def main():

    # passive
    serial_util.send_as_bytes(b'\x80')

    # safe mode
    serial_util.send_as_bytes(b'\x82')

    # full control
    serial_util.send_as_bytes(b'\x84')

    serial_util.send_as_bytes(b'\x8c\x00\x01\x4e\x10')
    serial_util.send_as_bytes(b'\x8d\x00')


if __name__ == "__main__":
    main()
