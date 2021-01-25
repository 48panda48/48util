import BinRW
#file=input("which file?")
#fl=fileRW(file)
from tkinter import *
def save():
    if text.get("0.0",END).replace(" ","").replace("\t","").replace("\n","").replace("0","").replace("1","") != "":
        saving=""
        for i in text.get("0.0",END).replace(" ","").replace("\t","").replace("\n",""): 
            saving+="{0:04b}".format(int(i,16))
    else:
        saving=text.get("0.0",END).replace(" ","").replace("\t","").replace("\n","")
    BinRW.write(file.get(),saving)
def load():
    set_input(BinRW.read(file.get()))
    print(BinRW.read(file.get()))
def set_input(value):
    text.delete(1.0, END)
    text.insert(END, value)
root = Tk()
Label(root,text="file:").grid(row=0,column=0 ,sticky=N+S+E+W)
file=Entry(root)
Button(root,text="Save",command=save).grid(row=0,column=2 ,sticky=N+S+E+W)
Button(root,text="Load",command=load).grid(row=0,column=3 ,sticky=N+S+E+W)
file.grid(row=0,column=1,sticky=N+S+E+W)
text = Text(root)
text.grid(column=0,row=1,sticky=N+S+E+W, columnspan=4)
Grid.columnconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 1, weight=1)
root.mainloop()
