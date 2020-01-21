from screen import *
from colorama import *
import numpy as np
from gameObject import *

class Mando(gameObj):
    def __init__(self):

        super().__init__()

        self.img = np.array([[" "," ", Back.BLACK+'O'], [Back.BLACK+'[', Back.BLACK+']', Back.BLACK+'|'], 
        [' ', ' ',Back.BLACK+ 'L']])
        self.x = 5
        self.y = 5
        self.width = 3
        self.height = 3
        self.vel = np.array([0, 0], dtype='float64')
        self.acc = np.array([0, 0.115], dtype='float64')
        self.lives = 5
        self.score = 0
        self.boostOn = 0
        self.boostCnt = 0
        self.regularGame = 0
        self.done = 0

    def checkCollision(self,objList,ind):

        for o in objList:
            
            if(o.objType == "magnet"):
                continue

            r1 = range(self.x,self.x+self.width+1)
            r2 = range(o.x,o.x+o.width+1)

            r3 = range(self.y,self.y+self.height+1)
            r4 = range(o.y,o.y+o.height+1)

            s1 = set(r1)
            s2 = set(r3)

            if(s1.intersection(r2) and s2.intersection(r4)):
                objList.remove(o)
                ind -= 1

                if(o.objType == "yoda"):
                    self.done = 1

                elif(o.objType == "beam"):
                    self.lives -= 1
                
                elif(o.objType == "coin"):
                    self.score += 50
                
                elif(o.objType == "boost"):
                    self.boostOn = 1
                    self.boostCnt = 1
        
        return ind
    
    def checkAlive(self):
        if(self.lives == 0):
            print(self.score)
            sys.exit(0)

    def shieldActivate(self,on,curr_lives):
        if(on):
            curr_lives = self.lives
            self.lives += 1000

            self.img = np.array([[" "," ", Back.BLUE+'O'], [Back.BLUE+'[', Back.BLUE+']', Back.BLUE+'|'], 
            [' ', ' ',Back.BLUE+ 'L']])
        else:
            self.lives = curr_lives
            self.img = np.array([[" "," ", Back.BLACK+'O'], [Back.BLACK+'[', Back.BLACK+']', Back.BLACK+'|'], 
            [' ', ' ',Back.BLACK+ 'L']])
        
        return curr_lives
    
    def getLives(self):
        return self.lives

    def setLives(self,new_lives):
        self.lives = new_lives
    
    def getScore(self):
        return self.lives
    
    def setScore(self,new_score):
        self.score = new_score
    
    def setBoostOn(self,new_b):
        self.boostOn = new_b
    
    def getBoostOn(self):
        return self.boostOn
    
    def setBoostCnt(self,new_b):
        self.boostCnt = new_b
    
    def getBoostCnt(self):
        return self.boostCnt
    
    def getDone(self):
        return self.done
    
    def setDone(self,new_done):
        self.done = new_done
    
    def getGame(self):
        return self.regularGame
    
    def setGame(self,new_game):
        self.regularGame = new_game