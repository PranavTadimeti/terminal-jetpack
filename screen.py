from colorama import *
import sys
import numpy as np


class Screen:

    def __init__(self, ht, wdt, display):
        self.display = display
        self.wdt = wdt
        self.ht = ht
        self.gnd = int((self.ht*4)/5)

    def createScreen(self):
        self.display[:] = " "+Back.BLUE

        # for i in range(self.gnd,self.ht):
        #     for j in range(self.wdt):
        #         self.display[i,j] = " "+Back.GREEN

        self.display[self.gnd:self.ht,:] = " "+Back.GREEN

    def printScreen(self):

        s = ''.join(str(c) for l in self.display for c in l)
        print(s)

        print("\033[0;0H")
        