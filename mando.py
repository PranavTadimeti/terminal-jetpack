from screen import *
from colorama import *
import numpy as np
from gameObject import gameObj

class Mando(gameObj):
    def __init__(self):
        gameObj.__init__(self) 
        self.img = np.array([[' ',' ','O'],['[',']','|'],[' ',' ','L']], dtype='str')
        self.x = 5
        self.y = 5
        
    def printMando(self,s):
        for i in range(3):
            for j in range(3):
                s.display[self.y+i,self.x+j] = self.img[i,j]

    
    def changeX(self,new_x,s):
        
        if(new_x > s.wdt-3 or new_x < 0):
            return
        
        for i in range(3):
            for j in range(3):
                s.display[self.y+i,self.x+j] = ' '

        self.x = new_x
    
    def changeY(self,new_y,s):

        if(new_y > s.ht-13 or new_y < 0):
            return

        for i in range(3):
            for j in range(3):
                s.display[self.y+i,self.x+j] = ' '

        self.y = new_y

         
    
