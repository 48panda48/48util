def encode(encode):
    all_freq = {} 
    for i in encode: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    while len(all_freq.items())>1:
        a=min(all_freq.items(), key=lambda x: x[1])
        del all_freq[a[0]]
        b=min(all_freq.items(), key=lambda x: x[1])
        del all_freq[b[0]]
        all_freq[(a[0],b[0])]=a[1]+b[1]
    tree=list(all_freq.keys())[0]
    def getpath(lst, target):
        for index, item in enumerate(lst):
            if item == target:
                return [index]
            if isinstance(item, (list, tuple)):
                path = getpath(item, target)
                if path:
                    return [index] + path
    def encodeItem(item):
        if isinstance(item, (list, tuple)):
            return "0" + encodeItem(item[0]) + encodeItem(item[1])
        else:
            if len("{0:08b}".format(ord(item)))==8:
                return "1" + "{0:08b}".format(ord(item))
            else:
                raise ValueError(f"{item} Not supported, must be less than unicode code 256.")
    binary=""
    for i in encode:
        for j in getpath(tree,i):
            binary+=str(j)
    return encodeItem(tree)+binary
def decode(decode):
    def decodeTree(remainingBits):
        if remainingBits[0]=="1":
            return chr(int(remainingBits[1:9],2)),remainingBits[9:]
        elif remainingBits[0]=="0":
            zero,remainingBits=decodeTree(remainingBits[1:])
            one,remainingBits=decodeTree(remainingBits)
            return (zero,one),remainingBits
    tree,binary=decodeTree(decode)
    text=""
    current=tree
    for i in binary:
        if type(current[int(i)])==tuple:
            current=current[int(i)]
        else:
            text+=current[int(i)]
            current=tree 
    return text
