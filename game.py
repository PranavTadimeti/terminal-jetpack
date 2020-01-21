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
from babyYoda import *

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
m.setGame(1)
yodaMade = 0

# game loop
while(True):

    y = m.getY()
    x = m.getX()

    # print("SCORE: ",m.getScore(),"\tLIVES: ",m.getLives())
    print(y,x)

    d.createScreen(m.getGame())

    if(cnt % 60 == 0 and m.getGame()):
        t = Beams(d, ind)
        objList.append(t)
        t.pickType()
        ind += 1

    if(cnt % 100 == 0 and m.getGame()):

        for i in range(6):
            objList.append(Coin(d, ind))
            ind += 1

        for j in range(ind-5, ind):

            if(ind-6 >= 0):
                objList[j].changeX(objList[ind-6].getX()+(j-ind+6), d)
                objList[j].changeY(objList[ind-6].getY(), d)

    if(cnt % 2000 == 0 and m.getGame()):
        sp = Boost(d, ind)
        objList.append(sp)
        ind += 1
 
    if(cnt  == 100 and m.getGame()):
        tempMag = Magnet(d)
        objList.append(tempMag)
        ind += 1
    
    if(cnt == 1000):
        bo = Boss(d,m)
        m.setGame(0)
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
        if(j.getObjType() == "magnet"):
            j.attract(m)

    if(m.getXVel() > 1.5):
        m.changeXVel(1.5)
    elif(m.getXVel() < -1.5):
        m.changeXVel(-1.5)

    m.changeX(m.getX()+int(m.getXVel()), d)

    m.changeYVel(m.getYVel()+m.getYAcc())

    if(m.getYVel() > 1):
        m.changeYVel(1)
    elif(m.getYVel() < -1.5):
        m.changeYVel(-1.5)

    if(m.getBoostCnt() < 200):
        m.setBoostCnt(m.getBoostCnt()+1)
    else:
        m.setBoostOn(0)

    for j in objList:
        j.changeX(j.getX()+j.getXVel(), d)
        ind = j.removeObj(objList, ind, d)

        if(m.getBoostOn() and (j.getObjType() != "bullet" and j.getObjType() != "boost" and j.getObjType() != "boss")):
            j.changeXVel(j.getXVel()-1)

    for j in objList:

        if(j.getObjType() == "bullet"):
            ind = j.checkCollision(objList, ind)
        elif(j.getObjType() == "bossBullet"):
            ind = j.checkCollision(objList,m,ind)

    
    for j in objList:
        d.renderObject(j)
    
    if(m.getGame() == 0 and bo.getLives() > 0):
        if(cnt % 50 == 0):
            tempBullet = bossBullet(d,ind)
            objList.append(tempBullet)
            ind += 1

            tempBullet.createBullet(bo.getX(),bo.getY(),m)

        bo.changeY(m.getY(),d)

    elif(m.getGame() == 0 and bo.getLives() == 0 and not yodaMade):
        yoda = babyYoda(d,ind)
        objList.append(yoda)
        ind += 1
        yodaMade = 1
            

    m.changeY(m.getY()+int(m.getYVel()), d)

    ind = m.checkCollision(objList, ind)

    if(m.getDone()):
        break

    m.checkAlive()

    d.renderObject(m)
    d.printScreen()

    cnt += 1

    time.sleep(0.018)

os.system('clear')

print("Won, you have")

