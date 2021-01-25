import random
from bitstring import BitArray

def readbits(filename):
    with open(filename,"rb") as f:
        input_str=f.read()
    c = BitArray(hex=input_str.hex())
    pad = ""
    if len(c.bin[2])%8!=0:
        topad=8-len(c.bin[2])
        pad = "0"*topad
    return c.bin
def writebits(filename,bits):
    the_bytearray=bytearray(int(bits[x:x+8], 2) for x in range(0, len(bits), 8))
    with open(filename, 'wb') as f:
        f.write(the_bytearray)
def seedfrompassword(password):
    random.seed(password)
    return random.randint(0,2**32)
