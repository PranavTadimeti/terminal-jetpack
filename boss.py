from screen import *
from colorama import *
import numpy as np
from gameObject import *

class Boss(gameObj):
    
    def __init__(self,s,m):

        super().__init__()

         
            
        tempStr =   r"""           
            ,===:'.,            `-._
                `:.`---.__         `-._
                    `:.     `--.         `.
                    \.        `.         `.
            (,,(,    \.         `.   ____,-`.,
            (,'     `/   \.   ,--.___`.'
        ,  ,'  ,--.  `,   \.;'         `
        `{D, {    \  :    \;
        V,,'    /  /    //
        j;;    /  ,' ,-//.    ,---.      ,
        \;'   /  ,' /  _  \  /  _  \   ,'/
                \   `'  / \  `'  / \  `.' /
                `.___,'   `.__,'   `.__,'"""  
        
        tempStr2 = tempStr.split('\n')
        
        self._img = []

        for j in tempStr2:
            temp = []
            for i in j:
                temp.append(i)
            
            self._img.append(temp)

        m = 0
        for a in self._img:
            if(len(a) > m):
                m = len(a)

        for a in self._img:
            while(m - len(a) > 0):
                a.append(' ')
        
        self._img = np.array(self._img)

        for i in self._img:
            for j in i:
                j = Back.BLACK+j

        self._x = s.getWidth()-50

        self._y = s.getGnd()-50

        self._height = 14
        self._width = 46

        self._objType = "boss"

        self._lives = 30

    def getLives(self):
        return self._lives
    
    def setLives(self,new_lives):
        self._lives = new_lives