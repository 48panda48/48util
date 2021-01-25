from bitstring import BitArray
from functools import reduce
import random
def encode(originalbits,repeat=1000):
    random.seed(originalbits)
    seed=192+random.randint(0,63)
    random.seed(seed)
    binary=bin(seed)[2:].zfill(8)+bin(repeat)[2:].zfill(16)
    bits_shuffling=originalbits
    num_bits=len(originalbits)
    for i in range(repeat):
        a=random.randint(1,num_bits-4)
        b=random.randint(a+1,num_bits-2)
        bits_shuffling=bits_shuffling[a:b]+bits_shuffling[:a]+bits_shuffling[b:]
    return binary+bits_shuffling
def decode(originalbits):
    seed=int(originalbits[:8],2)
    originalbits=originalbits[8:]
    repeat=int(originalbits[:16],2)
    originalbits=originalbits[16:]
    random.seed(seed)
    binary=""
    bits_shuffling=originalbits
    num_bits=len(originalbits)
    listab=[]
    for i in range(repeat):
        a=random.randint(1,num_bits-4)
        b=random.randint(a+1,num_bits-2)
        listab.append((a,b))
    listab=listab[::-1]
    for i in listab:
        a=i[0]
        b=i[1]
        bits_shuffling=bits_shuffling[b-a:b]+bits_shuffling[:b-a]+bits_shuffling[b:]
    random.seed(bits_shuffling)
    assert 192+random.randint(0,63)==seed,"error: bit was changed"
    return bits_shuffling
