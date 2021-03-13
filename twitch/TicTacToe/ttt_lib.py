from random import *
from playsound import playsound
from helpermodules.image_drawer import *
from handler import *
from time import *


def sound(type):
    pygame.event.pump()
    set_given("Game Off")

    try:
        if type == "tie":
            sounds = ["tie1", "tie2"]
            playsound("sounds/" + choice(sounds) + ".mp3", False)
        if type == "loss":
            sounds = ["loss1", "loss2", "loss3"]
            playsound("sounds/" + choice(sounds) + ".mp3", False)
        if type == "win":
            sounds = ["win1", "win2", "secret"]
            sound = choice(sounds)
            if sound != "secret":
                playsound("sounds/" + sound + ".mp3", False)
            if sound == "secret":
                draw_image("secret", 0, 0)
                playsound("sounds/" + sound + ".mp3", False)
                start = monotonic()
                while monotonic() - start < 210:
                    pygame.event.pump()
    except:
        pass


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

            if a == "G":
                a = "X"
            if b == "G":
                b = "X"
            if c == "G":
                c = "X"

            if a == "X" or b == "X" or c == "X":
                if a == "X" and b == "X" and c != "X" and c != "O":
                    t = pw[2]
                    if fields[t] == "-":
                        return t
                if a == "X" and c == "X" and b != "X" and b != "O":
                    t = pw[1]
                    if fields[t] == "-":
                        return t
                if b == "X" and c == "X" and a != "X" and a != "O":
                    t = pw[0]
                    if fields[t] == "-":
                        return t

        for pw in pws:
            a = fields[pw[0]]
            b = fields[pw[1]]
            c = fields[pw[2]]

            if a == "G":
                a = "O"
            if b == "G":
                b = "O"
            if c == "G":
                c = "O"

            if a == "O" or b == "O" or c == "O":
                if a == "O" and b == "O" and c != "O" and c != "X":
                    t = pw[2]
                    if fields[t] == "-":
                        return t
                if a == "O" and c == "O" and b != "O" and b != "X":
                    t = pw[1]
                    if fields[t] == "-":
                        return t
                if b == "O" and c == "O" and a != "O" and a != "X":
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
                    if c == "X" and a != "X" and a != "O" and b == "-":
                        t = choice([pw[0], pw[1]])
                    if b == "X" and a != "X" and a != "O" and c == "-":
                        t = choice([pw[2], pw[0]])

        if fields[t] == "O" or fields[t] == "X":
            return ai(fields)

        if fields[t] == "-":
            return t
        else:
            return ai(fields)
    except:
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
        XScore = 0
        OScore = 0
        for x in y:
            if fields[x] == "G":
                XScore += 1
                OScore += 1
            if fields[x] == "X":
                XScore += 1
            if fields[x] == "O":
                OScore += 1
            if XScore == 3:
                return 1
            if OScore == 3:
                return 2


def getin():
    pygame.event.pump()
    while 1:
        pygame.event.pump()
        given = read_given()
        print(given)
        if keydown(K_KP1) or keydown(K_7) or given == "7":
            return 1
        if keydown(K_KP2) or keydown(K_8) or given == "8":
            return 2
        if keydown(K_KP3) or keydown(K_9) or given == "9":
            return 3
        if keydown(K_KP4) or keydown(K_4) or given == "4":
            return 4
        if keydown(K_KP5) or keydown(K_5) or given == "5":
            return 5
        if keydown(K_KP6) or keydown(K_6) or given == "6":
            return 6
        if keydown(K_KP7) or keydown(K_1) or given == "1":
            return 7
        if keydown(K_KP8) or keydown(K_2) or given == "2":
            return 8
        if keydown(K_KP9) or keydown(K_3) or given == "3":
            return 9


def word(thing):
    pygame.event.pump()
    if thing == 1:
        return "one"
    if thing == 2:
        return "two"
    if thing == 3:
        return "three"
    if thing == 4:
        return "four"
    if thing == 5:
        return "five"
    if thing == 6:
        return "six"
    if thing == 7:
        return "seven"
    if thing == 8:
        return "eight"
    if thing == 9:
        return "nine"


def ds(fields):
    c = color(0, 0, 0)
    x1, x2, x3 = fields[0], fields[1], fields[2]
    x4, x5, x6 = fields[3], fields[4], fields[5]
    x7, x8, x9 = fields[6], fields[7], fields[8]
    x = [[x1, 0, 0], [x2, 50, 0], [x3, 100, 0], [x4, 0, 50],
         [x5, 50, 50], [x6, 100, 50], [x7, 0, 100],
         [x8, 50, 100], [x9, 100, 100]]

    pygame.event.pump()
    index = 0
    for i in x:
        index += 1
        pygame.event.pump()

        thing = "error"

        if i[0] == "-":
            thing = word(index)
        if i[0] == "O":
            thing = "green"
        if i[0] == "X":
            thing = "red"
        if i[0] == "G":
            thing = "gold"

        draw_image(thing, i[1] + int(320 / 3) - 20, i[2] + int(222 / 3) - 40)
