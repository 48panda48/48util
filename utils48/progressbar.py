import tkinter
from tkinter import ttk
from datetime import datetime
import time
def getQuad(n):
    j=0
    for i in range(n+1):
        j+=i^2
    return j
class progress:
    def __init__(self,total=100,length=400,timebar=False,timeestimate=True,quadratic=False):#enable timebar if time between updates varies, uses time left estimate to generate, rather than percentage(NOTE:percentage is used, but yeah)
        self.root = tkinter.Tk()
        self.pb = ttk.Progressbar(self.root,length=length)
        self.pb.pack()
        if timeestimate:
            self.text=tkinter.Button(self.root)
            self.text.pack()
        self.showing=(timebar,timeestimate)
        self.total=total
        self.root.update()
        self.timestart=datetime.utcnow()
        self.quad=False
        if quadratic:
            self.total=getQuad(total)
            self.quad=True
    def update(self,upto):
        try:
            if self.quad:
                upto=getQuad(upto)
            percent=upto*100/self.total
            now=datetime.utcnow()
            dist=now-self.timestart
            estTotal=dist*100/percent
            estToGo=estTotal-dist
            self.timestart=now
            if not self.showing[0]:
                self.pb["value"]=upto*100/self.total
            else:
                self.pb["value"]=dist*100/estTotal
            self.pb.pack()
            if self.showing[1]:
                self.text.destroy()
                self.text=tkinter.Button(self.root,text=str(estToGo)[:7])
                self.text.pack()
            self.root.update()
            if upto>=self.total:
                self.destroy()
        except:
            pass
    def destroy(self):
        self.root.destroy()