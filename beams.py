from screen import *
from gameObject import *
import numpy as np
from random import randint,randrange,random


class Beams(gameObj):

    def __init__(self,s):
        self.img = np.array(['@','@','@','@','@'])
        self.s = s
        self.x = s.wdt-5
        self.y = randrange(self.s.ht-10)
        self.sz = 5
        

    def printBeam(self):

        for j in range(self.sz):
            self.s.display[self.y,self.x+j] = self.img[j]
        
    



        