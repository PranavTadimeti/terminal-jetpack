from colorama import *
import sys
import numpy as np

class Screen:
   
    def __init__(self,ht,wdt,display):
        self.display = display
        self.wdt = wdt
        self.ht = ht
    
    def createScreen(self):
        self.display[:] = ' '   

         

    def printScreen(self):

        print(Back.BLUE)
        s = ''.join(str(c) for l in self.display for c in l)

        print(s[0:(self.ht-10)*self.wdt],end="\r")

        print(Back.GREEN)
        print(s[(self.ht-10)*self.wdt:(self.ht*self.wdt)],end="\r")
            
        print("\033[0;0H")

            
            
            
            