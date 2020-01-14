import colorama
from colorama import init
from colorama import Fore, Back, Style
import sys
from screen import *
from mando import *
from gameObject import *
import os
import signal
import time
from alarmex import AlarmException
from inp import getCh

r, c = os.popen('stty size', 'r').read().split()
r = int(r)-3
c = int(c)

init()

d = Screen(r, c, np.array([[' ' for i in range(c)]
                           for j in range(r)], dtype='str'))
d.createScreen()

m = Mando()


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


cnt = time.time()

while(True):

    flying = 0

    m.printMando(d)
    d.printScreen()

    inp = move()

    y = m.getY()
    x = m.getX()

    if(inp == 'w'):
        flying = 1
        m.changeY(y-2, d)
        cnt = time.time()

    elif(inp == 's'):
        m.changeY(y+2, d)

    elif(inp == 'a'):
        m.changeX(x-1, d)

    elif(inp == 'd'):
        m.changeX(x+1, d)

    elif(inp == 'q'):
        sys.exit(0)

    if(not flying):
        m.changeY(int(y+(time.time()/cnt)), d)
