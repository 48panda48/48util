from bitstring import BitArray
from functools import reduce
import random
from utils import seedfrompassword
def encode(originalbits,password):
    seed=64+seedfrompassword(password)
    random.seed(seed)
    binary="01010101"
    n=8
    for byte in [originalbits[i:i+n] for i in range(0, len(originalbits), n)]:
        byte_int=int(byte,2)
        randnum=random.randint(0,255)
        byte_int=(byte_int + randnum)%256
        binary += bin(byte_int)[2:].zfill(8)
    return binary
def decode(originalbits,password):
    seed=64+seedfrompassword(password)
    originalbits=originalbits[8:]
    random.seed(seed)
    binary=""
    n=8
    for byte in [originalbits[i:i+n] for i in range(0, len(originalbits), n)]:
        byte_int=int(byte,2)
        randnum=random.randint(0,255)
        byte_int=(byte_int - randnum)%256
        binary += bin(byte_int)[2:].zfill(8)
    random.seed(binary)
    return binary
