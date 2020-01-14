from screen import *
from colorama import *
import numpy as np


class gameObj:

    def __init__(self):
        self.img = []
    
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
        
    def changeX(self,new_x,s):
        self.x = new_x
        
    def changeY(self,new_y,s):
        self.y = new_y