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
from bullets import *
from magnet import *
from speedBoost import *

r, c = os.popen('stty size', 'r').read().split()
r = int(r)-3
c = int(c)

init() 

d = Screen(r, c, np.full((r, c), Back.BLUE+" "))

m = Mando()

kb = KBHit()

objList = []
cnt = 0
ind = 0
flag = 0
shield = 0
mag = 0
speedCnt = 0

# game loop
while(True):
    flying = 0

    y = m.getY()
    x = m.getX()
    
    d.createScreen()

    if(cnt%60 == 0):
        t = Beams(d,ind)
        objList.append(t)
        t.pickType()
        ind += 1
    
    if(cnt%100 == 0):
        
        for i in range(6):
            objList.append(Coin(d,ind))
            ind += 1
        
        for j in range(ind-5,ind):
            
            if(ind-6 >= 0):
                objList[j].changeX(objList[ind-6].getX()+(j-ind+6),d)
                objList[j].changeY(objList[ind-6].getY(),d)

    if(cnt%2000 == 0):
        sp = Boost(d,ind)
        objList.append(sp)
        ind += 1

    if(shield == 2):
        if(time.time() - tim >= 60):
            shield = 0
    
    elif(shield == 1):
        if(time.time() - tim >= 10):
            m.shieldActivate(0,curr_lives)
            shield = 2
            tim = time.time()
    
    if kb.kbhit():
        
        inp = kb.getch()

        if(ord(inp) == 27):
            break

        elif(inp == 'w'):
            flying = 1
            m.changeYVel(-1.25)
            m.changeXVel(0)

        elif(inp == 's'):
            m.changeYVel(1)
            m.changeXVel(0)

        elif(inp == 'a'):
            m.changeXVel(-1.5)

        elif(inp == 'd'):
            m.changeXVel(1.5)
        
        elif(inp == 'l'):
            v = Bullet(d,ind)
            objList.append(v)
            ind += 1

            v.createBullet(m.getX()+3,m.getY()+1)
        
        elif(inp == ' '):
            if(shield == 0):
                tim = time.time()
                shield = 1
                curr_lives = m.shieldActivate(1,0)

        m.changeX(m.getX()+int(m.getXVel()), d)
    
    if(m.boostCnt < 200):
        m.boostCnt += 1
    else:
        m.boostOn = 0
        
    for j in objList:
        j.changeX(j.getX()+j.getXVel(),d)
        ind = j.removeObj(objList,ind,d)

        if(m.boostOn and (j.objType != "bullet" and j.objType != "boost")):
            j.changeXVel(j.getXVel()-1)

    if(not flying):

        if(m.getYVel() <= 1):
            m.changeYVel(m.getYVel()+m.acc[1])
        else:
            m.changeYVel(1)


    for j in objList:

        if(j.objType == "bullet"):
            ind = j.checkCollision(objList,ind)
        
        elif(j.objType == "magnet"):
            j.attract(m)
    
    for j in objList:
        j.printObject(d)
    
    else:
        mag = 0

    m.changeY(m.getY()+int(m.getYVel()), d)

    ind = m.checkCollision(objList,ind)

    m.checkAlive()

    m.printObject(d)
    d.printScreen()

    cnt += 1

    time.sleep(0.018)
