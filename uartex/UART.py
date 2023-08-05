from serial import Serial

'''
REQUIREMENTS:
Package    Version
---------- -------
pip        22.3.1
pyserial   3.5
setuptools 65.5.1
wheel      0.38.4
'''


def read_until_end_char(serial_object, start_char, end_char):
    data = b''
    read_mode = False
    while True:
        received_byte = serial_object.read()
        if not read_mode and received_byte == start_char.encode():
            read_mode = True
        if read_mode:
            data += received_byte
            if received_byte == end_char.encode():
                read_mode = False
                break
    return data.decode('utf-8')


def write_message(serial_object, message):
    if isinstance(serial_object, Serial):
        serial_object.write(message)
    else:
        return Exception("Serial communication is not open!")
