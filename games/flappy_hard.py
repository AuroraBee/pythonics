from math import *
from helpermodules.kandinsky import *
from time import *
from helpermodules.ion import *
from random import *
from pygame.constants import *


def pl(hsc, d):
    pygame.event.pump()
    Star = 1
    dx, dy = [], []
    for i in range(4):
        dx.append(randint(0, 320))
        dy.append(randint(0, 222))
    pygame.event.pump()
    cht, chro, chd, chst = 1, 1, 1, 0
    stx, sty, std, stth, stv, stev = [], [], [], [], [], []
    px, py = [], []
    rx, ry = [], []
    for i in range(1):
        px.append(randint(0, 320))
        py.append(randint(0, 222))
        rx.append(randint(-6, 6))
        ry.append(randint(-6, 6))
    pygame.event.pump()
    fr = False
    ob = color(0, 0, 0)
    w = color(255, 255, 255)
    b = ob
    ev = 7
    ft = 30
    r = 5
    pygame.event.pump()
    ppp = [0, 0]
    tow = [[55, 45], [20, 35], [15, 45], [35, 55], [100, 40], [140, 35], [100, 25], [100, 40], [100, 35], [100, 55]]
    list = [30, 35, 40]
    pos = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 30, 45, 40, 35, 35, 35, 50, 45, 115,
           120]
    da = False
    t = choice(tow)
    for i in range(len(tow) * 2):
        t = [choice(pos), choice(list)]
        tow.append(t)
        pygame.event.pump()
    tu, tl = int(t[0] / 2), int(t[1] * 0.75)
    x = 15
    y = 220
    vy = -16
    g = 2
    pp = [x, y]
    j = True
    p = 2
    v = 2
    jt = 1
    sc = r
    for i in range(1280 * 555):
        pygame.event.pump()
        th = int(20 + int(r * 1.25) + int(v * 1.5) * 2)
        if fr:
            th = int(th * 20)
        if keydown(K_d):
            x += 3
        if keydown(K_a):
            x -= 2
        if keydown(K_s) and sc >= 5:
            sc -= 7.5
            ft += 5
        draw_string("Score:", 0, 0)
        draw_string(str([int(sc), int(hsc)]), 10 * 6, 0)
        sleep(0.05)
        pygame.event.pump()
        if sc > hsc:
            hsc = sc
        vy += g
        y += vy
        pygame.event.pump()
        # /// stx,sty,std,stth,stv,stev

        if chst:
            for i in range(std):
                stv[i] = v
                stev[i] = ev
                stth[i] = 15

        # ///
        pygame.event.pump()
        # ///

        if chro:
            for i in range(len(ry)):
                if px[i] > x:
                    rx[i] -= 1
                if px[i] < x:
                    rx[i] += 1
                if py[i] > y:
                    ry[i] -= 1
                if py[i] < y:
                    ry[i] += 1
                px[i] += rx[i]
                py[i] += ry[i]
                rx[i] = (rx[i] / 1.05)
                ry[i] = (ry[i] / 1.05)
                fill_rect(int(px[i]), int(py[i]), 2, 2, ob)

        # ///
        pygame.event.pump()
        # ///

        if chd:
            for i in range(len(dx)):
                if dx[i] > x:
                    dx[i] -= 0.25
                if dx[i] < x:
                    dx[i] += 0.25
                if dy[i] > y:
                    dy[i] -= 0.25
                if dy[i] < y:
                    dy[i] += 0.25
                fill_rect(int(dx[i]), int(dy[i]), 2, 2, b)

        # ///
        pygame.event.pump()
        if keydown(K_SPACE) and j:
            j = False
            vy = -10
            jt = 1
        elif keydown(K_w) and ft > 0:
            ft -= 1.5
            vy = -g + 2
        elif not j and not keydown(K_SPACE):
            j = True
        elif not j and keydown(K_SPACE):
            vy -= floor(5 / jt)
            jt += 3
        if not keydown(K_w) and ft < 10:
            ft += 0.2
        p = int(p + v + ev)
        pygame.event.pump()
        th = int(th * 1.5)
        if cht:
            fill_rect(320 - p, 0, th, 222, b)
            fill_rect(320 - p - th, 0, ceil(v + ev + th), 222, w)
            fill_rect(320 - p + th, 0, ceil(v + ev + th), 222, w)
            fill_rect(320 - p, tu, th, tl, w)
        fill_rect(int(ppp[0]), int(ppp[1]), 5, 5, color(255, 255, 255))
        fill_rect(int(pp[0]), int(pp[1]), 5, 5, color(150, 150, 150))
        pygame.event.pump()
        ppp = [pp[0], pp[1]]
        pp = [x, y]
        fill_rect(int(x), int(y), 5, 5, ob)
        if p > 320 + th:
            ev = 0
            p = 320
            sc += v + r
            r += 1
            v *= -1.2
            fr = False
            t = choice(tow)
            tu, tl = int(t[0] * 1.15), int(t[1] * (2 - (r / 100)))
        pygame.event.pump()
        if p < 0:
            ev = 0
            p = 0
            sc += v + r
            r += 1
            v *= -1.3
            fr = False
            t = choice(tow)
            tu, tl = int(t[0] * 1.15), int(t[1] * (2 - (r / 100)))
        pygame.event.pump()
        if keydown(K_KP7):
            brea(50, 4, 1)
            hsc *= 2
            draw_string("Cheats--Nope!", 50, 0)
        pygame.event.pump()
        if keydown(K_v):
            ev += 2
        if v >= (int(r * 1.5)):
            if v >= 5:
                v = v / (2 + (r / v))
                if v <= 1:
                    v = 5
        if 320 - p <= x <= 320 - p + th:
            da = True
            pygame.event.pump()
        else:
            pygame.event.pump()
            if da:
                ev += int(v * 2)
                ft += int((v + (r / v)) / 25)
            da = False
        if get_pixel(int(x - 1), int(y + 2)) == b:
            brea()
            d += 1
            return hsc, d
        if get_pixel(int(x + 6), int(y + 2)) == b:
            brea()
            d += 1
            return hsc, d
        pygame.event.pump()
        if get_pixel(int(x - 1), int(y + 2)) == ob:
            brea()
            d += 1
            return hsc, d
        if get_pixel(int(x + 6), int(y + 2)) == ob:
            brea()
            d += 1
            return hsc, d
        if 320 - p + th < x:
            ev = v * 3.5
        draw_string("Trys:", 0, 200)
        draw_string(str(d), 50, 200)
        draw_string("Float-Time:", 0, 16)
        draw_string(str(int(int((ft * 0.04) * 100)) / 100), 110, 16)
        pygame.event.pump()
        while Star:
            pygame.event.pump()
            draw_string("Home-to-start", 0, 200)
            if keydown(K_SPACE):
                Star = 0


def brea(r=200, bb=9, bw=1):
    pygame.event.pump()
    b = color(0, 0, 0)
    w = color(255, 255, 255)
    l = []
    for i in range(bb):
        l.append(b)
    for i in range(bw):
        l.append(w)
    for x in range(r):
        for y in range(r):
            set_pixel(randint(0, 320), randint(0, 222), choice(l))


def tst(d):
    pygame.event.pump()
    if d <= 1:
        return choice(
            ["Blocky-Bird Ultra-Edition", "Blocky-Bird Deluxe-Edition", "Blocky-Bird Rekt-Edition", "Not-Flappy Bird",
             "Dark Birds: The Rektening", "Blocky-Bird: Death Edition"])
    if 5 >= d > 1:
        li = ["You cannot win!", "Oopsie, watch the missile!", "Bad performance...", "Balls, you died!"]
        return choice(li)
    if 10 >= d > 5:
        li = [rw(randint(2, 4)), "What are you trying to gain", "Stop trying, Noob!", "The walls have eyes (;-;)",
              "<{0v0}> *Snaps your Neck*"]
        return choice(li)
    if 15 >= d > 10:
        li = ["What a waste of time", "(0xU) (cant beat me)", "Get Rekt", "Youre worm food"]
        return choice(li)
    if 20 >= d > 15:
        li = [rw(randint(3, 6)), "3Sp00ky5U", "GET NO-SCOPED", "Damn, son!", "Dark Souls: FLOPPY BLOCK"]
        return choice(li)
    if 25 >= d > 20:
        li = [rw(randint(5, 8)), "Bad spawn? Too bad!", "Oof, that was close!", "RATLANTEANS", "DOOM: ETERNAL FLOPPING"]
        return choice(li)
    if 30 >= d > 25:
        li = [rw(randint(4, 7)), rw(randint(4, 7)), "You cant do it!", "Do give up!", "Dont be calm ;3",
              "THE MISSILE KNOWS WERE IT IS BECAUSE IT KNOWS WHERE IT ISNT"]
        return choice(li)
    if 35 >= d > 30:
        li = [rw(randint(5, 7)), rw(randint(5, 7)), rw(randint(4, 5)), "Welcome, welcome to HELL",
              "H.ighly E.njoyable \n L.ight L.aughing", "We hope you enjoy your stay", "And good RIDDANCE"]
        return choice(li)
    if d > 35:
        li = [rw(randint(8, 25)), rw(randint(8, 25)), rw(randint(8, 25)), rw(randint(8, 25)), rw(randint(8, 25)),
              rw(randint(8, 25)), rw(randint(8, 25)), rw(randint(8, 25)), rw(randint(8, 25)), rw(randint(8, 25)),
              rw(randint(8, 25)), rw(randint(8, 25)), rw(randint(8, 25))]
        return choice(li)


def rw(le=5):
    pygame.event.pump()
    v = ["A", "E", "I", "O", "U", "M", "N", "O", "S"]
    n = ["B", "D", "G", "H", "K", "P", "T", "F", "R", "L"]
    w = ""
    for i in range(le):
        w = w + choice(n)
        for i in range(randint(1, 3)):
            w = w + choice(v)
    return w


def sta(sc, d, fs=False):
    pygame.event.pump()
    b = color(0, 0, 0)
    done = False
    w = color(255, 255, 255)
    pla = False
    tex = False
    if fs:
        pygame.event.pump()
        fill_rect(-10, -10, 330, 232, color(250, 250, 250))
        fill_rect(0, 0, 320, 222, w)
        for i in range(20):
            pygame.event.pump()
            fill_rect(i * 4, 222 - (i * 4), 4, 4, b)
        fill_rect(5 * 4, 5 * 4, 4, 4, b)
        fill_rect(6 * 4, 7 * 4, 4, 4, b)
        fill_rect(6 * 4, 8 * 4, 4, 4, b)
        fill_rect(5 * 4, 10 * 4, 4, 4, b)
        fill_rect(66, 0, 14, 222, b)
        fill_rect(66, 110, 14, 30, w)
        fill_rect(120, 0, 35, 222, b)
        fill_rect(120, 35, 35, 40, w)
        fill_rect(280, 0, 44, 222, b)
        fill_rect(280, 180, 44, 25, w)
        fill_rect(40, 85, 10, 10, b)
        brea(200, 7, 3)
        pygame.event.pump()
    while not pla:
        pygame.event.pump()
        # brea(5,24,1)
        if keydown(K_SPACE) and tex:
            pygame.event.pump()
            if choice([False, True, True, True, True]) or d < 3:
                pygame.event.pump()
                brea(150, 0, 10)
                for x in range(320):
                    for y in range(222):
                        pygame.event.pump()
                        set_pixel(x, y, w)
            else:
                fill_rect(0, 0, 320, 222, w)
                pygame.event.pump()
            return pl(sc, d)
        if not pla:
            pygame.event.pump()
            if not done:
                pygame.event.pump()
                draw_string(tst(d), 160 - 110 - d, 111 - 50)
                done = True
            draw_string("Press OK to play", 90, 111)
            draw_string("Score:", 120, 150)
            draw_string(str(sc), 120 + (10 * 6), 150)
            draw_string("Try:", 120, 170)
            draw_string(str(d), 160, 170)
            tex = True


def a(sc, d, fs):
    while True:
        pygame.event.pump()
        sc, d = sta(int(sc), d, fs)
        fs = False


pygame.event.pump()
a(16, 1, True)
