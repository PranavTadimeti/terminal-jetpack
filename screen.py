import math
from colorama import *
import sys
import numpy as np


class Screen:

    def __init__(self, height, width, display):
        self._display = display
        self._width = width
        self._height = height
        self._gnd = int((self._height*4)/5)

    def createScreen(self,regularGame):

        if(not regularGame):
            self._display[0:self._height,:] = Back.BLACK+" "
        else:
            self._display[0:self._height,:] = Back.CYAN+" "
        
        self._display[self._gnd:self._height,:] = Back.GREEN+" "

    def printScreen(self):

        s = ''.join(str(c) for l in self._display for c in l)
        print(s)

        print("\033[0;0H")
    
    def getWidth(self):
        return self._width
    
    def getHeight(self):
        return self._height
    
    def getGnd(self):
        return self._gnd
    
    def renderObject(self,obj):

        for i in range(obj.getHeight()):
            for j in range(obj.getWidth()):
                self._display[obj.getY()+i, obj.getX()+j] = obj.sliceImg(i,j)
         
    def createDragon(self,c,pos,ht):
        
        a = np.linspace(-math.pi/2,math.pi/2,pos)
        f = (np.sin(a+math.pi*c)+1)*(ht/2)

        cnt = 0
        for i in f:
            cnt += 1
            self._display[int(i),cnt] = Back.WHITE+'O'