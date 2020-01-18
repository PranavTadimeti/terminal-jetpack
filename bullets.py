from colorama import *
from screen import *
from gameObject import *
import numpy as np


class Bullet(gameObj):

    def __init__(self,s,index):
        self.img = np.full((1,1),Back.MAGENTA+"D")
        self.s = s
        self.x = 0
        self.y = 0
        self.width = 1
        self.height = 1
        self.vel = np.array([0,0])
        self.acc = np.array([0,0])
        self.index = index
        self.objType = "bullet"

    def createBullet(self,x,y):
        self.x = x
        self.y = y
        self.vel = [3,0]