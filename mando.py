from screen import *
from colorama import *
import numpy as np
from gameObject import *


class Mando(gameObj):
    def __init__(self):
        self.img = np.array([[" "," ", Back.BLACK+'O'], [Back.BLACK+'[', Back.BLACK+']', Back.BLACK+'|'], 
        [' ', ' ',Back.BLACK+ 'L']])
        self.x = 5
        self.y = 5
        self.width = 3
        self.height = 3
        self.vel = np.array([0, 0], dtype='float64')
        self.acc = np.array([0, 0.115], dtype='float64')
