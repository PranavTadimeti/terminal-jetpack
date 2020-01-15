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

"""
def move():
    def alarmhandler(signum, frame):
        ''' input method '''
        raise AlarmException

    def user_input(timeout=0.15):
        ''' input method '''
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)

        try:
            text = getCh()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    ch = user_input()

    return ch
"""

kb = KBHit()

cnt = 0
beamcnt = 0
beamsList = []

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
            cnt = 0
            m.changeY(y-2, d)

        elif(inp == 's'):
            m.changeY(y+2, d)

        elif(inp == 'a'):
            m.changeX(x-1, d)

        elif(inp == 'd'):
            m.changeX(x+1, d)

    # inp = move()

    if(not flying):
        cnt += 1
        m.changeY(int(y+cnt), d)

    time.sleep(0.01)
