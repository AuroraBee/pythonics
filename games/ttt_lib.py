from random import *
from pygame.constants import *
from helpermodules.kandi import *

fields = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"]


def sfi(fields):
    l = []
    for i in range(9):
        if fields[i] == "-":
            l.append(inp(i + 1))
    return l


# 7,8,9
# 4,5,6
# 1,2,3

def smai(fields):
    pygame.event.pump()
    pws = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
    t = 0
    try:
        for pw in pws:
            a = fields[pw[0]]
            b = fields[pw[1]]
            c = fields[pw[2]]

            if a == "X" or b == "X" or c == "X":
                print("Att", pw, a, b, c)
                if a == "X" and b == "X" and c != "X" and c != "O":
                    t = pw[2]
                    print("Found 2-X, commencing Fortnite Dance.")
                    if fields[t] == "-":
                        return t
                if a == "X" and c == "X" and b != "X" and b != "O":
                    t = pw[1]
                    print("Found 2-X, commencing Fortnite Dance.")
                    if fields[t] == "-":
                        return t
                if b == "X" and c == "X" and a != "X" and a != "O":
                    t = pw[0]
                    print("Found 2-X, commencing Fortnite Dance.")
                    if fields[t] == "-":
                        return t

        for pw in pws:
            a = fields[pw[0]]
            b = fields[pw[1]]
            c = fields[pw[2]]

            if a == "O" or b == "O" or c == "O":
                print("Def", pw, a, b, c)
                if a == "O" and b == "O" and c != "O" and c != "X":
                    print("Blocking 2-O on", t)
                    t = pw[2]
                    if fields[t] == "-":
                        return t
                if a == "O" and c == "O" and b != "O" and b != "X":
                    print("Blocking 2-O on", t)
                    t = pw[1]
                    if fields[t] == "-":
                        return t
                if b == "O" and c == "O" and a != "O" and a != "X":
                    print("Blocking 2-O on", t)
                    t = pw[0]
                    if fields[t] == "-":
                        return t

        for pw in pws:
            a = fields[pw[0]]
            b = fields[pw[1]]
            c = fields[pw[2]]

            if t == 0:
                if a == "X" or b == "X" or c == "X":
                    if a == "X" and c != "X" and c != "O" and b == "-":
                        t = choice([pw[2], pw[1]])
                        print("Preping  to win")
                    if c == "X" and a != "X" and a != "O" and b == "-":
                        t = choice([pw[0], pw[1]])
                        print("Performing randomness")
                    if b == "X" and a != "X" and a != "O" and c == "-":
                        t = choice([pw[2], pw[0]])
                        print("Confusing human")

        if fields[t] == "O" or fields[t] == "X":
            print("Spot taken")
            return ai(fields)

        if fields[t] == "-":
            return t
        else:
            print("UwU, second empty check")
            return ai(fields)
    except:
        print("AI Broke, prolly a draw.")
        return ai(fields)


def ai(fields):
    for i in range(100):
        pygame.event.pump()
        p = randint(0, 8)
        if fields[p] == "-":
            return p
    raise Exception('AI found Nothing.')


def inp(inpu):
    pygame.event.pump()
    if inpu == 1:
        return 7
    elif inpu == 2:
        return 8
    elif inpu == 3:
        return 9
    elif inpu == 9:
        return 3
    elif inpu == 8:
        return 2
    elif inpu == 7:
        return 1
    else:
        return inpu


def cw(fields):
    pygame.event.pump()
    pw = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for y in pw:
        c = 0
        for x in y:
            if fields[x] == "X":
                c -= 1
            if fields[x] == "O":
                c += 1
            if c == -3:
                print("X Wins")
                return 1
            if c == 3:
                print("O Wins")
                return 2


def getin():
    pygame.event.pump()
    while 1:
        pygame.event.pump()
        if keydown(K_KP1):
            return 1
        if keydown(K_KP2):
            return 2
        if keydown(K_KP3):
            return 3
        if keydown(K_KP4):
            return 4
        if keydown(K_KP5):
            return 5
        if keydown(K_KP6):
            return 6
        if keydown(K_KP7):
            return 7
        if keydown(K_KP8):
            return 8
        if keydown(K_KP9):
            return 9
        if keydown(K_KP0):
            return 0


def ds(fields):
    c = color(0, 0, 0)
    x1, x2, x3 = fields[0], fields[1], fields[2]
    x4, x5, x6 = fields[3], fields[4], fields[5]
    x7, x8, x9 = fields[6], fields[7], fields[8]
    x = [[x1, 0, 0], [x2, 50, 0], [x3, 100, 0], [x4, 0, 50],
         [x5, 50, 50], [x6, 100, 50], [x7, 0, 100],
         [x8, 50, 100], [x9, 100, 100]]

    pygame.event.pump()
    for i in x:
        if i[0] == "-":
            c = color(0, 80, 115)
        if i[0] == "O":
            c = color(50, 255, 50)
        if i[0] == "X":
            c = color(255, 50, 0)

        fill_rect(i[1] + int(320 / 3) - 20, i[2] + int(222 / 3) - 40, 45, 45, c)
