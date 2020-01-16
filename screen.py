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
        self.display[0:self.ht,:] = Back.CYAN+" "
        self.display[self.gnd:self.ht,:] = Back.GREEN+" "

    def printScreen(self):

        s = ''.join(str(c) for l in self.display for c in l)
        print(s)

        print("\033[0;0H")
        