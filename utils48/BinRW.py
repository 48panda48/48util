from array import *
def read(file):
    with open(file, "rb") as f:
        data = list(bytearray(f.read()))
    result = ""
    for i in data:
        result += "{0:08b}".format(i)
    if result[:3] != "000":
        result = result[:-int(result[:3],2)]
    result = result[3:]
    return result
def write(file,bin_to_add):
    bin_array = array('B')
    bin_to_add= "{0:03b}".format((8-((len(bin_to_add)+3)%8))%8) + bin_to_add
    bin_to_add+="0000000"
    for i in [bin_to_add[i:i+8] for i in range(0, len(bin_to_add)-7, 8)]:
        bin_array.append(int(i,2))
    with open(file,'wb+') as f:
        bin_array.tofile(f)
def append(file,bin_to_add):
    write(file, read(file) + bin_to_add)
def getsize(bin_to_add):
    bin_array = array('B')
    bin_to_add= "{0:03b}".format((8-((len(bin_to_add)+3)%8))%8) + bin_to_add
    bin_to_add+="0000000"
    for i in [bin_to_add[i:i+8] for i in range(0, len(bin_to_add)-7, 8)]:
        bin_array.append(int(i,2))
    B=len(bin_array)
    kB=B/1024
    mB=kB/1024
    return B
class fileRW:
    def __init__(self,file):
        self.file=file
    def __lshift__(self,other):
        if type(other) != str:
            return NotImplemented
        if len(other.replace("0","").replace("1",""))>0:
            raise ValueError("string contains more than 0s and 1s")
        write(self.file,other)
    def __iadd__(self,other):
        if type(other) != str:
            return NotImplemented
        if len(other.replace("0","").replace("1",""))>0:
            raise ValueError("string contains more than 0s and 1s")
        append(self.file,other)
        return self
    def __invert__(self):
        return str(self)
    def __str__(self):
        return read(self.file)
    def __repr__(self):
        return read(self.file)
