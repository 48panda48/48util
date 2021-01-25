import random
def encode(originalbits):
    random.seed(originalbits)
    seed=128+random.randint(0,63)
    random.seed(seed)
    binary=bin(seed)[2:].zfill(8)
    n=8
    for byte in [originalbits[i:i+n] for i in range(0, len(originalbits), n)]:
        byte_int=int(byte,2)
        randnum=random.randint(0,255)
        byte_int=byte_int ^ randnum
        binary += bin(byte_int)[2:].zfill(8)
    return binary
def decode(originalbits):
    seed=int(originalbits[:8],2)
    originalbits=originalbits[8:]
    random.seed(seed)
    binary=""
    n=8
    for byte in [originalbits[i:i+n] for i in range(0, len(originalbits), n)]:
        byte_int=int(byte,2)
        randnum=random.randint(0,255)
        byte_int=byte_int ^ randnum
        binary += bin(byte_int)[2:].zfill(8)
    random.seed(binary)
    assert 128+random.randint(0,63)==seed,"error: bit was changed"
    return binary
