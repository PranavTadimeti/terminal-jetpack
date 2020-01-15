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
        self.display[:] = ' '

    def printScreen(self):

        print(Back.BLUE)
        s = ''.join(str(c) for l in self.display for c in l)

        print(s[0:self.gnd*self.wdt], end="\r")

        print(Back.GREEN)
        print(s[self.gnd*self.wdt:(self.ht*self.wdt)], end="\r")

        print("\033[0;0H")
