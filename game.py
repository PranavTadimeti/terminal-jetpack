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
from boss import *
from bossBullets import *

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

    y = m.getY()
    x = m.getX()

    d.createScreen(m.bossFight)

    if(cnt % 60 == 0 and not m.bossFight):
        t = Beams(d, ind)
        objList.append(t)
        t.pickType()
        ind += 1

    if(cnt % 100 == 0 and not m.bossFight):

        for i in range(6):
            objList.append(Coin(d, ind))
            ind += 1

        for j in range(ind-5, ind):

            if(ind-6 >= 0):
                objList[j].changeX(objList[ind-6].getX()+(j-ind+6), d)
                objList[j].changeY(objList[ind-6].getY(), d)

    if(cnt % 2000 == 0 and not m.bossFight):
        sp = Boost(d, ind)
        objList.append(sp)
        ind += 1
 
    if(cnt  == 3000 and not m.bossFight):
        tempMag = Magnet(d)
        objList.append(tempMag)
        ind += 1
    
    if(cnt == 1000):
        bo = Boss(d,m)
        m.bossFight = 1
        objList.append(bo)
        ind += 1

    if(shield == 2):
        if(time.time() - tim >= 60):
            shield = 0

    elif(shield == 1):
        if(time.time() - tim >= 10):
            m.shieldActivate(0, curr_lives)
            shield = 2
            tim = time.time()

    m.changeXVel(0)

    if kb.kbhit():

        inp = kb.getch()

        if(ord(inp) == 27):
            break

        elif(inp == 'w'):
            m.changeYVel(m.getYVel()-5)
            m.changeXVel(0)

        elif(inp == 's'):
            m.changeYVel(m.getYVel()+0.5)
            m.changeXVel(0)

        elif(inp == 'a'):
            m.changeXVel(m.getXVel()-1.5)

        elif(inp == 'd'):
            m.changeXVel(m.getXVel()+1.5)

        elif(inp == 'l'):
            v = Bullet(d, ind)
            objList.append(v)
            ind += 1

            v.createBullet(m.getX()+3, m.getY()+1)

        elif(inp == ' '):
            if(shield == 0):
                tim = time.time()
                shield = 1
                curr_lives = m.shieldActivate(1, 0)

    for j in objList:
        if(j.objType == "magnet"):
            j.attract(m)

    if(m.getXVel() > 1.5):
        m.changeXVel(1.5)
    elif(m.getXVel() < -1.5):
        m.changeXVel(-1.5)

    m.changeX(m.getX()+int(m.getXVel()), d)

    m.changeYVel(m.getYVel()+m.acc[1])

    if(m.getYVel() > 1):
        m.changeYVel(1)
    elif(m.getYVel() < -1):
        m.changeYVel(-1)

    if(m.boostCnt < 200):
        m.boostCnt += 1
    else:
        m.boostOn = 0

    for j in objList:
        j.changeX(j.getX()+j.getXVel(), d)
        ind = j.removeObj(objList, ind, d)

        if(m.boostOn and (j.objType != "bullet" and j.objType != "boost" and j.objType != "boss")):
            j.changeXVel(j.getXVel()-1)

    for j in objList:

        if(j.objType == "bullet"):
            ind = j.checkCollision(objList, ind)
        elif(j.objType == "bossBullet"):
            ind = j.checkCollision(objList,m,ind)

    
    for j in objList:
        j.printObject(d)
    
    if(m.bossFight):
        if(cnt % 50 == 0):
            tempBullet = bossBullet(d,ind)
            objList.append(tempBullet)
            ind += 1

            tempBullet.createBullet(bo.getX(),bo.getY(),m)

        bo.changeY(m.getY(),d)

        if(bo.lives == 0):
            m.bossFight = 0
            break

    m.changeY(m.getY()+int(m.getYVel()), d)

    ind = m.checkCollision(objList, ind)

    m.checkAlive()

    m.printObject(d)
    d.printScreen()

    cnt += 1

    time.sleep(0.018)

print(Back.BLACK)
print("YOU WIN!!!")
