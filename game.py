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
from coins import *

r, c = os.popen('stty size', 'r').read().split()
r = int(r)-3
c = int(c)

init()

d = Screen(r, c, np.full((r, c), Back.BLUE+" "))

m = Mando()

kb = KBHit()

objList = []
bcnt = 0
ccnt = 0
ind = 0

# game loop
while(True):
    flying = 0

    y = m.getY()
    x = m.getX()
    
    d.createScreen()

    if(bcnt%60 == 0):
        t = Beams(d,ind)
        objList.append(t)
        t.pickType()
        ind += 1

    if(ccnt%100 == 0):
        objList.append(Coin(d,ind))
        ind += 1
    
    for j in objList:
        j.printObject(d)
        j.changeX(j.getX()+j.getXVel(),d)



    m.printObject(d)
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

        m.changeX(m.getX()+int(m.getXVel()), d)

    if(not flying):

        if(m.getYVel() <= 1.75):
            m.changeYVel(m.getYVel()+m.acc[1])

    m.changeY(m.getY()+int(m.getYVel()), d)

    bcnt += 1
    ccnt += 1

    for j in objList:
        j.removeObj(objList)

    time.sleep(0.02)
