import colorama
from colorama import init
from colorama import Fore, Back, Style
import sys
from screen import *
from mando import *
from gameObject import *
from beams import *
import os
import signal
import time
from alarmex import AlarmException
from inp import getCh
from asynch import KBHit

r, c = os.popen('stty size', 'r').read().split()
r = int(r)-3
c = int(c)

init()

d = Screen(r, c, np.array([[' ' for i in range(c)]
                           for j in range(r)], dtype='str'))
d.createScreen()

m = Mando()

kb = KBHit()

cnt = 0
beamcnt = 0
beamsList = []


#game loop
while(True):

    flying = 0

    y = m.getY()
    x = m.getX()

    m.printMando(d)
    d.printScreen()
    
    if kb.kbhit():

        inp = kb.getch()

        if(ord(inp) == 27):
            break

        elif(inp == 'w'):
            flying = 1
            m.changeYVel(-1)
            m.changeXVel(0)

        elif(inp == 's'):
            m.changeYVel(1)
            m.changeXVel(0)

        elif(inp == 'a'):
            m.changeXVel(-1)

        elif(inp == 'd'):            
            m.changeXVel(1)
        
        m.changeX(m.getX()+int(m.getXVel()),d)

    if(not flying):
        m.changeYVel(m.getYVel()+m.acc[1])
        # m.changeY(m.getY()+m.getYVel(),d)
    
    m.changeY(m.getY()+int(m.getYVel()),d)
        
    
    time.sleep(0.02)
