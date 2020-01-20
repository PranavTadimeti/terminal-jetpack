from screen import *
from colorama import *
import numpy as np
from gameObject import *

class Boss(gameObj):
    
    def __init__(self,s,m):

        super().__init__()

         
        tempStr =       r"""        
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
        
        self.img = []

        for j in tempStr2:
            temp = []
            for i in j:
                temp.append(i)
            
            self.img.append(temp)

        m = 0
        for a in self.img:
            if(len(a) > m):
                m = len(a)

        for a in self.img:
            while(m - len(a) > 0):
                a.append(' ')
        
        self.img = np.array(self.img)

        print(np.shape(self.img))

        for i in self.img:
            for j in i:
                j = Back.BLACK+j

        self.x = s.width-80

        self.y = s.gnd-50

        self.height = 14
        self.width = 70

# b = Boss(d,m)