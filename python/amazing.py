#! env python
#
# + The original program is by Jack Hauber, and the source is
#   "Basic Computer Games." Used with permission of David Ahl;
#   see www.SwapMeetDave.com.
# + This exercise was inspired by Alan Hensel's use of Amazing
#   as a refactoring challenge.
# + This transliteration to Ruby was created by Kevin Rutherford,
#   kevin@rutherford-software.com
#

import random

target = 0                      # where GOTO goes
result = ''

def clear():
    global result
    result = ''

def println():
    global result
    result = result + '\n'

def write(text):
    global result
    result = result + text

def rnd(count):
    return random.randint(1, count+1)

def goto(lineno):
    global target
    target = lineno

def doit(horizontal, vertical):
    global target
    global result
    target = 0
    result = ''

    clear
    write('Amazing - Copyright by Creative Computing, Morristown, NJ')
    println()

    h = horizontal
    v = vertical
    if h == 1 or v == 1:
        return

    wArray = [[0 for x in range(v+1)] for y in range(h+1)]
    vArray = [[0 for x in range(v+1)] for y in range(h+1)]

    q = 0
    z = 0
    x = rnd(h)

    # 130:170
    for i in range(1, h+1):
        if i == x:
            write(':  ')
        else:
            write(':--')

    # 180
    write(':')
    println()

    # 190
    c = 1
    wArray[x][1] = c
    c = c+1

    # 200
    r = x
    s = 1
    goto(270)

    while target != -1:
        if target == 210:
            if r != h:
                goto(250)
            else:
                goto(220)
        elif target == 220:
            if s != v:
                goto(240)
            else:
                goto(230)
        elif target == 230:
            r = 1
            s = 1
            goto(260)
        elif target == 240:
            r = 1
            s = s+1
            goto(260)
        elif target == 250:
            r = r+1
            goto(260)
        elif target == 260:
            if wArray[r][s] == 0:
                goto(210)
            else:
                goto(270)
        elif target == 270:
            if r - 1 == 0:
                goto(600)
            else:
                goto(280)
        elif target == 280:
            if wArray[r - 1][s] != 0:
                goto(600)
            else:
                goto(290)
        elif target == 290:
            if s - 1 == 0:
                goto(430)
            else:
                goto(300)
        elif target == 300:
            if wArray[r][s - 1] != 0:
                goto(430)
            else:
                goto(310)
        elif target == 310:
            if r == h:
                goto(350)
            else:
                goto(320)
        elif target == 320:
            if wArray[r + 1][s] != 0:
                goto(350)
            else:
                goto(330)
        elif target == 330:
            x = rnd(3)
            goto(340)
        elif target == 340:
            if x == 1:
                goto(940)
            elif x == 2:
                goto(980)
            elif x == 3:
                goto(1020)
            else:
                goto(350)
        elif target == 350:
            if s != v:
                goto(380)
            else:
                goto(360)
        elif target == 360:
            if z == 1:
                goto(410)
            else:
                goto(370)
        elif target == 370:
            q = 1
            goto(390)
        elif target == 380:
            if wArray[r][s + 1] != 0:
                goto(410)
            else:
                goto(390)
        elif target == 390:
            x = rnd(3)
            goto(400)
        elif target == 400:
            if x == 1:
                goto(940)
            elif x == 2:
                goto(980)
            elif x == 3:
                goto(1090)
            else:
                goto(410)
        elif target == 410:
            x = rnd(2)
            goto(420)
        elif target == 420:
            if x == 1:
                goto(940)
            elif x == 2:
                goto(980)
            else:
                goto(430)
        elif target == 430:
            if r == h:
                goto(530)
            else:
                goto(440)
        elif target == 440:
            if wArray[r + 1][s] != 0:
                goto(530)
            else:
                goto(450)
        elif target == 450:
            if s != v:
                goto(480)
            else:
                goto(460)
        elif target == 460:
            if z == 1:
                goto(510)
            else:
                goto(470)
        elif target == 470:
            q = 1
            goto(490)
        elif target == 480:
            if wArray[r][s + 1] != 0:
                goto(510)
            else:
                goto(490)
        elif target == 490:
            x = rnd(3)
            goto(500)
        elif target == 500:
            if x == 1:
                goto(940)
            elif x == 2:
                goto(1020)
            elif x == 3:
                goto(1090)
            else:
                goto(510)
        elif target == 510:
            x = rnd(2)
            goto(520)
        elif target == 520:
            if x == 1:
                goto(940)
            elif x == 2:
                goto(1020)
            else:
                goto(530)
        elif target == 530:
            if s != v:
                goto(560)
            else:
                goto(540)
        elif target == 540:
            if z == 1:
                goto(590)
            else:
                goto(550)
        elif target == 550:
            q = 1
            goto(570)
        elif target == 560:
            if wArray[r][s + 1] != 0:
                goto(590)
            else:
                goto(570)
        elif target == 570:
            x = rnd(2)
            goto(580)
        elif target == 580:
            if x == 1:
                goto(940)
            elif x == 2:
                goto(1090)
            else:
                goto(590)
        elif target == 590:
            goto(940)
        elif target == 600:
            if s - 1 == 0:
                goto(790)
            else:
                goto(610)
        elif target == 610:
            if wArray[r][s - 1] != 0:
                goto(790)
            else:
                goto(620)
        elif target == 620:
            if r == h:
                goto(720)
            else:
                goto(630)
        elif target == 630:
            if wArray[r + 1][s] != 0:
                goto(720)
            else:
                goto(640)
        elif target == 640:
            if s != v:
                goto(670)
            else:
                goto(650)
        elif target == 650:
            if z == 1:
                goto(700)
            else:
                goto(660)
        elif target == 660:
            q = 1
            goto(680)
        elif target == 670:
            if wArray[r][s + 1] != 0:
                goto(700)
            else:
                goto(680)
        elif target == 680:
            x = rnd(3)
            goto(690)
        elif target == 690:
            if x == 1:
                goto(980)
            elif x == 2:
                goto(1020)
            elif x == 3:
                goto(1090)
            else:
                goto(700)
        elif target == 700:
            x = rnd(2)
            goto(710)
        elif target == 710:
            if x == 1:
                goto(980)
            elif x == 2:
                goto(1020)
            else:
                goto(720)
        elif target == 720:
            if s != v:
                goto(750)
            else:
                goto(730)
        elif target == 730:
            if z == 1:
                goto(780)
            else:
                goto(740)
        elif target == 740:
            q = 1
            goto(760)
        elif target == 750:
            if wArray[r][s + 1] != 0:
                goto(780)
            else:
                goto(760)
        elif target == 760:
            x = rnd(2)
            goto(770)
        elif target == 770:
            if x == 1:
                goto(980)
            elif x == 2:
                goto(1090)
            else:
                goto(780)
        elif target == 780:
            goto(980)
        elif target == 790:
            if r == h:
                goto(880)
            else:
                goto(800)
        elif target == 800:
            if wArray[r + 1][s] != 0:
                goto(880)
            else:
                goto(810)
        elif target == 810:
            if s != v:
                goto(840)
            else:
                goto(820)
        elif target == 820:
            if z == 1:
                goto(870)
            else:
                goto(830)
        elif target == 830:
            q = 1
            goto(990)
        elif target == 840:
            if wArray[r][s + 1] != 0:
                goto(870)
            else:
                goto(850)
        elif target == 850:
            x = rnd(2)
            goto(860)
        elif target == 860:
            if x == 1:
                goto(1020)
            elif x == 2:
                goto(1090)
            else:
                goto(870)
        elif target == 870:
            goto(1020)
        elif target == 880:
            if s != v:
                goto(910)
            else:
                goto(890)
        elif target == 890:
            if z == 1:
                goto(930)
            else:
                goto(900)
        elif target == 900:
            q = 1
            goto(920)
        elif target == 910:
            if wArray[r][s + 1] != 0:
                goto(930)
            else:
                goto(920)
        elif target == 920:
            goto(1090)
        elif target == 930:
            goto(1190)
        elif target == 940:
            wArray[r - 1][s] = c
            goto(950)
        elif target == 950:
            c = c+1
            vArray[r - 1][s] = 2
            r = r-1
            goto(960)
        elif target == 960:
            if c == h * v + 1:
                goto(1200)
            else:
                goto(970)
        elif target == 970:
            q = 0
            goto(270)
        elif target == 980:
            wArray[r][s - 1] = c
            goto(990)
        elif target == 990:
            c = c+1
            goto(1000)
        elif target == 1000:
            vArray[r][s - 1] = 1
            s = s-1
            if c == h * v + 1:
                goto(1200)
            else:
                goto(1010)
        elif target == 1010:
            q = 0
            goto(270)
        elif target == 1020:
            wArray[r + 1][s] = c
            goto(1030)
        elif target == 1030:
            c = c+1
            if vArray[r][s] == 0:
                goto(1050)
            else:
                goto(1040)
        elif target == 1040:
            vArray[r][s] = 3
            goto(1060)
        elif target == 1050:
            vArray[r][s] = 2
            goto(1060)
        elif target == 1060:
            r = r+1
            goto(1070)
        elif target == 1070:
            if c == h * v + 1:
                goto(1200)
            else:
                goto(1080)
        elif target == 1080:
            goto(600)
        elif target == 1090:
            if q == 1:
                goto(1150)
            else:
                goto(1100)
        elif target == 1100:
            wArray[r][s + 1] = c
            c = c+1
            if vArray[r][s] == 0:
                goto(1120)
            else:
                goto(1110)
        elif target == 1110:
            vArray[r][s] = 3
            goto(1130)
        elif target == 1120:
            vArray[r][s] = 1
            goto(1130)
        elif target == 1130:
            s = s+1
            if c == v * h + 1:
                goto(1200)
            else:
                goto(1140)
        elif target == 1140:
            goto(270)
        elif target == 1150:
            z = 1
            goto(1160)
        elif target == 1160:
            if vArray[r][s] == 0:
                goto(1180)
            else:
                goto(1170)
        elif target == 1170:
            vArray[r][s] = 3
            q = 0
            goto(1190)
        elif target == 1180:
            vArray[r][s] = 1
            q = 0
            r = 1
            s = 1
            goto(260)
        elif target == 1190:
            goto(210)
        elif target == 1200:
            target = -1

    for j in range(1, v+1):
        write('I')
        for i in range(1, h+1):
            if vArray[i][j] >= 2:
                write('   ')
            else:
                write('  I')
        write(' ')
        println()
        for i in range(1, h+1):
            if vArray[i][j] == 0:
                write(':--')
            elif vArray[i][j] == 2:
                write(':--')
            else:
                write(':  ')
        write(':')
        println()

if __name__ == '__main__':
    doit(10, 10)
    print result

