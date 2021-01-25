from utils import *
import random
import add
import xor
import shuffle
def encrypt(encode,password):
        to_encode="00111111"+encode
        left=[0,1,2]
        while len(left)>0:
            random.seed(password)
            next_inseq = left[random.randint(0,len(left)-1)]
            left.remove(next_inseq)
            if next_inseq==0:
                to_encode=xor.encode(to_encode)
            if next_inseq==1:
                to_encode=shuffle.encode(to_encode)
            if next_inseq==2:
                to_encode=add.encode(to_encode,password)
        return to_encode
def decrypt(encode,password):
        to_encode=encode
        left=[0,1,2]
        order=[]
        while len(left)>0:
            random.seed(password)
            next_inseq = left[random.randint(0,len(left)-1)]
            left.remove(next_inseq)
            order.append(next_inseq)
        for next_inseq in order[::-1]:
            if next_inseq==0:
                to_encode=xor.decode(to_encode)
            if next_inseq==1:
                to_encode=shuffle.decode(to_encode)
            if next_inseq==2:
                to_encode=add.decode(to_encode,password)
        assert to_encode[:8]=="00111111","wrong password, data invalid"
        return to_encode[8:]
def ShellInputs():
    encode_or_decode=input("do you want to encrypt or decrypt?")
    while encode_or_decode.lower() not in ["encrypt","decrypt"]:
        encode_or_decode=input("do you want to encrypt or decrypt?")
    type_to_encode=input(f"do you want to {encode_or_decode} a file or binary?")
    while type_to_encode.lower() not in ["file","binary"]:
        type_to_encode=input(f"do you want to {encode_or_decode} a file or binary?")
    if encode_or_decode=="encrypt":
        if type_to_encode=="file":
            to_encode=readbits(input("Which file to encrypt?"))
        if type_to_encode=="binary":
            to_encode=input("paste binary data")
            assert to_encode.replace("0","").replace("1","")=="","binary data is not binary data. chars:"+to_encode.replace("0","").replace("1","")
        password=input("please enter a secret password (people with it can decrypt)")
        encoded=encrypt(to_encode,password)
        file=input("output to file or shell?")
        while file.lower() not in ["file","shell"]:
            file=input("output to file or shell?")
        if file=="file":
            writebits(input("which file?"),encoded)
        else:
            print(encoded)
    else:
        if type_to_encode=="file":
            to_encode=readbits(input("Which file to encrypt?"))
        if type_to_encode=="binary":
            to_encode=input("paste binary data")
            assert to_encode.replace("0","").replace("1","")=="","binary data is not binary data. chars:"+to_encode.replace("0","").replace("1","")
        password=input("please enter the secret password")
        encoded=decrypt(to_encode,password)
        file=input("output to file or shell?")
        while file.lower() not in ["file","shell"]:
            file=input("output to file or shell?")
        if file=="file":
            writebits(input("which file?"),encoded)
        else:
            print(encode)
