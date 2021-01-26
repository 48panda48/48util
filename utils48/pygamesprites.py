import pygame
import time
class Part:
    def __init__(self,shape,surface,color,rect,identify=None):
        self.shape = shape
        self.identify=identify
        self.surface = surface
        self.color = color
        self.x = rect[0]
        self.y = rect[1]
        self.sizex = rect[2]
        self.sizey = rect[3]
    def draw(self):
        if self.shape == "ellipse":
            pygame.draw.ellipse(self.surface,self.color,(self.x,self.y,self.sizex,self.sizey))
        if self.shape == "rect":
            pygame.draw.rect(self.surface,self.color,(self.x,self.y,self.sizex,self.sizey))
    def move(self,x,y,relative=True):
        if relative:
            self.x += x
            self.y += y
        else:
            self.x = x
            self.y = y
    def resize(self,x,y,relative=True,centered=True):
        if relative:
            self.sizex += x
            self.sizey += y
        else:
            self.sizex = x
            self.sizey = y
        if centered:
            self.move(-x/2,-y/2)
class PartBox:
	def __init__(self,parts,HandleKeyboardEvents=False,game=None):
		self.game=game
		self.parts={}
		for i in parts:
			self.parts[i.identify] = i
	def __getitem__(self,key):
		 return self.parts[key]
	def __call__(self,val):
		self.parts[val.identify]=val
	def __add__(self,other):
		if type(other)==Part:
			self.__call__(other)
		elif type(other)==type(self):
			for i in list(other.parts.values()):
				self.__call__(i)
	def __radd__(self,other):
		self.__add__(other)
	def __iadd__(self,other):
		self.__add__(other)
	def drawall(self):
		self.game.fill((0,0,0))
		for i in list(self.parts.values()):
			i.draw()
		pygame.display.update()
	def moveall(self,x,y):
		for i in list(self.parts.values()):
			i.move(x,y)
		self.drawall()
	def scaleall(self,x,y,relative=True,centered=True):
		for i in list(self.parts.values()):
			i.resize(x,y,relative,centered)
		self.drawall()