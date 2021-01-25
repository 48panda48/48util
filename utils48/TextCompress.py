# there was a bug with the last one.
def encode(encode,notree=False):
    all_freq = {} 
    for i in encode: #generate a dictionary with form {"a":num of times a appears,"b":num of times a appears}
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    # this uses https://en.wikipedia.org/wiki/Huffman_coding
    while len(all_freq.items())>1:#while there are more than 1 items.
        a=min(all_freq.items(), key=lambda x: x[1])#get the least common item
        del all_freq[a[0]]
        b=min(all_freq.items(), key=lambda x: x[1])#get the second least common item
        del all_freq[b[0]]
        all_freq[(a[0],b[0])]=a[1]+b[1]#replace the least common item and the second least common item with an entry with them both in.
        # what this ends up with:
        # for the string "hello" it would be {(("h","e"),("o","l")):5}
        # the tree would be:
        #                base
        #              0/    \1
        #              *      *
        #            0/ \1  0/ \1
        #            h   e  o   l
        # to navigate the tree in python it would be tree[0][1] for "e" and tree[1][1] for "l"
    tree=list(all_freq.keys())[0]#extract the tree from the dict.
    if notree:
        tree=(((((((('j', 'q'), ('z', 'x')), 'v'), 'b'), 'c'), ((('k', 'w'), 'g'), 'l')), ('e', ('s', ('h', 'm')))), (((('p', 'd'), 'n'), ('t', 'o')), (((('y', 'f'), 'u'), 'i'), ('r', 'a'))))
    print(tree)
    def getpath(tree, target):# takes the tree and the letter and returns the path(in binary) to take e.g. getpath(tree,"o") returns "10"
        for index, item in enumerate(tree): #for both the items in the tree( or subtree)
            if item == target:# if it's what is needed return the path it took(a 1 or 0) 
                return str(index)
            if isinstance(item, (list, tuple)):# if it is a subtree, run this function.
                path = getpath(item, target)
                if path:# if target is in the subtree,
                    return str(index) + path # return the path from the subtree's base with how to get to the subtree's base from the tree's base.
        return False # if target not in tree, return false.
    def encodeItem(item): # takes an item (string or tuple/list) and encodes it.
        if isinstance(item, (list, tuple)):# if item is a subtree
            return "0" + encodeItem(item[0]) + encodeItem(item[1])# return 0 + item 1 in binary + item 2 in binary. The 0 is used to say that a tree is next
        else:
            if len("{0:08b}".format(ord(item)))==8:# if the character fits in 8 bits,
                return "1" + "{0:08b}".format(ord(item)) # return 1 + ord(char). The 1 is used to say the next 8 bits are a character.
            else:
                raise ValueError(f"{item} Not supported, must be less than unicode code 256.")# the reader would break if the character fits in more than 8 bits, as the decoder gives 8 bits to each character
    #EXAMPLE:
    # if we put in our tree for "hello"
    # we get "001011010001011001010101101111101101100"
    # if we format it it is
    #
    # 0 0 1 01101000   1 01100101      0 1 01101111   1 01101100
    # ( ( "     h   ", "     e   ") ,  ( "     o   ", "    l     ") )
    #               *1           *2 *3             *1            *2 *4
    #*1 : implied because char had 8 bits and first item of a tuple is done.
    #*2 : implied because char had 8 bits and second item of a tuple is done.
    #*3 : implied because first item of tuple is done
    #*4 : implied because second item of tuple is done. any following bits contain the message.
    binary=""
    for i in encode:
        binary+=getpath(tree,i) # get path through tree for each char
    if notree:
        return "0"+binary
    return "1"+encodeItem(tree)+binary#encode tree
def decode(decode):
    def decodeTree(remainingBits):# for decoding the tree the function gets the remaining bits and removes some and adds more to the tree.
        if remainingBits[0]=="1":#if first bit is 1 (it is decoding a string)
            return chr(int(remainingBits[1:9],2)),remainingBits[9:]# return the decoded character and the bits after the ones used(first 9)
        elif remainingBits[0]=="0":# if tuple should be made
            zero,remainingBits=decodeTree(remainingBits[1:])# get the first item by giving itself all but the first bit.
            one,remainingBits=decodeTree(remainingBits)# get the second item by giving itself all the first runthrough didn't use.
            return (zero,one),remainingBits # return the tuple and the remaining bits
    tree,binary=decodeTree(decode[1:])# get the tree and the binary(the text encoded)
    text=""
    if decode[0] == "0":
        binary=decode[1:]
        tree=(((((((('j', 'q'), ('z', 'x')), 'v'), 'b'), 'c'), ((('k', 'w'), 'g'), 'l')), ('e', ('s', ('h', 'm')))), (((('p', 'd'), 'n'), ('t', 'o')), (((('y', 'f'), 'u'), 'i'), ('r', 'a'))))
    current=tree#create a copy of tree
    for i in binary: # for each bit,
        if type(current[int(i)])==tuple:# if the path the bit sends us to is a tuple(more bits needed)
            current=current[int(i)]# narrow down the places the next char is by changing current
        else:# the bit tells us which char it is
            text+=current[int(i)]# add the char to the text
            current=tree # reset the current variable for the next bit
    return text # when finished return result
if __name__=="__main__":
    if input("e to encode, anything else to decode") == "e":
        enc = input("what would you like to encode?")
        print("here is the string of binary",encode(enc))
    else:
        dec = input("what do you want to decode?")
        print(decode(dec))
    # i do have a way of reading/writingbits to files (with more code i wrote), but i have not included it here. (i can send it to you if you want to see it though.)
