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
            m.acc[1] = 0
            m.changeYVel(-1)
            m.changeXVel(0)

        elif(inp == 's'):
            m.changeYVel(1)
            m.changeXVel(0)

        elif(inp == 'a'):
            m.changeXVel(-1)

        elif(inp == 'd'):            
            m.changeXVel(1)
        
        #Updating mando's properties

        m.changeX(m.getX()+m.getXVel(),d)
        m.changeY(m.getY()+m.getYVel(),d)

    if(not flying):
        m.acc[1] = 1
        m.changeYVel(m.getYVel()+m.acc[1])
        m.changeY(m.getY()+m.getYVel(),d)
        
    
    time.sleep(0.01)
