from screen import *
from colorama import *
import numpy as np
from gameObject import *


class Mando(gameObj):
    def __init__(self):
        self.img = np.array([[' ', ' ', 'O'], ['[', ']', '|'], [' ', ' ', 'L']], dtype='str')
        self.x = 5
        self.y = 5
        self.width = 3
        self.height = 3
        self.vel = np.array([0, 0], dtype='float64')
        self.acc = np.array([0, 0.15], dtype='float64')

    def printMando(self, s):

        for i in range(self.height):
            for j in range(self.width):

                s.display[int(self.y+i), int(self.x+j)] = self.img[i, j]
