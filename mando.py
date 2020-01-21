from screen import *
from colorama import *
import numpy as np
from gameObject import *

class Mando(gameObj):
    def __init__(self):

        super().__init__()

        self._img = np.array([[" "," ", Back.BLACK+'O'], [Back.BLACK+'[', Back.BLACK+']', Back.BLACK+'|'], 
        [' ', ' ',Back.BLACK+ 'L']])
        self._x = 5
        self._y = 5
        self._width = 3
        self._height = 3
        self._vel = np.array([0, 0], dtype='float64')
        self._acc = np.array([0, 0.115], dtype='float64')
        self._lives = 5
        self._score = 0
        self._boostOn = 0
        self._boostCnt = 0
        self._regularGame = 0
        self._done = 0

    def checkCollision(self,objList,ind):

        for o in objList:
            
            if(o.getObjType() == "magnet"):
                continue

            r1 = range(self._x,self._x+self._width+1)
            r2 = range(o.getX(),o.getX()+o.getWidth()+1)

            r3 = range(self._y,self._y+self._height+1)
            r4 = range(o.getY(),o.getY()+o.getHeight()+1)

            s1 = set(r1)
            s2 = set(r3)

            if(s1.intersection(r2) and s2.intersection(r4)):
                objList.remove(o)
                ind -= 1

                if(o.getObjType() == "yoda"):
                    self._done = 1

                elif(o.getObjType() == "beam"):
                    self._lives -= 1
                
                elif(o.getObjType() == "coin"):
                    self._score += 50
                
                elif(o.getObjType() == "boost"):
                    self._boostOn = 1
                    self._boostCnt = 1
        
        return ind
    
    def checkAlive(self):
        if(self._lives == 0):
            print(self._score)
            sys.exit(0)

    def shieldActivate(self,on,curr_lives):
        if(on):
            curr_lives = self._lives
            self._lives += 1000

            self._img = np.array([[" "," ", Back.BLUE+'O'], [Back.BLUE+'[', Back.BLUE+']', Back.BLUE+'|'], 
            [' ', ' ',Back.BLUE+ 'L']])
        else:
            self._lives = curr_lives
            self._img = np.array([[" "," ", Back.BLACK+'O'], [Back.BLACK+'[', Back.BLACK+']', Back.BLACK+'|'], 
            [' ', ' ',Back.BLACK+ 'L']])
        
        return curr_lives
    
    def getLives(self):
        return self._lives

    def setLives(self,new_lives):
        self._lives = new_lives
    
    def getScore(self):
        return self._lives
    
    def setScore(self,new_score):
        self._score = new_score
    
    def setBoostOn(self,new_b):
        self._boostOn = new_b
    
    def getBoostOn(self):
        return self._boostOn
    
    def setBoostCnt(self,new_b):
        self._boostCnt = new_b
    
    def getBoostCnt(self):
        return self._boostCnt
    
    def getDone(self):
        return self._done
    
    def setDone(self,new_done):
        self._done = new_done
    
    def getGame(self):
        return self._regularGame
    
    def setGame(self,new_game):
        self._regularGame = new_game