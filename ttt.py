from ttt_lib import *
from time import *

def big():
    return [69420, "Me Me Big Boi"]

# seed(1010)
def play():
    infinity = big()[0]
    fields = [
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

    # 7,8,9
    # 4,5,6
    # 1,2,3
    pygame.event.pump()
    bg = color(0, 50, 75)
    g = color(50, 200, 50)
    r = color(200, 50, 0)
    ti = color(75, 25, 200)
    tp = 0
    turn = 1
    fill_rect(0, 0, 320, 222, color(50, 50, 50))
    if 1:
        try:
            pygame.event.pump()
            fields[inp(ai(fields))] = "X"
        except:
            turn = 0
    for i in range(900):
        pygame.event.pump()
        print(fields[0], fields[1], fields[2])
        print(fields[3], fields[4], fields[5])
        print(fields[6], fields[7], fields[8])
        if turn:
            print("Turn O")
        else:
            print("Turn X")
        xx = 1
        while xx:
            if cw(fields) == 1:
                fill_rect(0, 0, 320, 222, r)
                ds(fields)
                raise Exception("AI won.")
            if cw(fields) == 2:
                fill_rect(0, 0, 320, 222, g)
                pygame.event.pump()
                ds(fields)
                raise Exception("Player won.")
            if sfi(fields) == []:
                print("Draw!")
                fill_rect(0, 0, 320, 222, ti)
                pygame.event.pump()
                ds(fields)
                raise Exception("Stalemate.")
            if tp:
                print("---_---_---")
                pygame.event.pump()
                ds(fields)
                place = getin()
            else:
                if turn:
                    pygame.event.pump()
                    ds(fields)
                    place = getin()
                else:
                    try:
                        pygame.event.pump()
                        t = smai(fields)
                        print("--", t)
                        place = 0
                        if fields[t] == "-":
                            fields[t] = "X"
                            pygame.event.pump()
                            ds(fields)
                            turn = True
                        else:
                            pygame.event.pump()
                            place = ai(fields)
                    except:
                        try:
                            pygame.event.pump()
                            place = ai(fields)
                        except:
                            print("Draw!")
                            fill_rect(0, 0, 320, 222, ti)
                            pygame.event.pump()
                            ds(fields)
                            raise Exception("Stalemate.")
            pygame.event.pump()
            place = inp(place)
            if place == 0:
                turn = True
                continue
            pygame.event.pump()
            pygame.event.pump()
            if fields[place - 1] == "-":
                pygame.event.pump()
                if turn:
                    fields[place - 1] = "O"
                    turn = False
                    xx = 0
                else:
                    fields[place - 1] = "X"
                    turn = True
                    xx = 0
            pygame.event.pump()
        ds(fields)


while 1:
    try:
        pygame.event.pump()
        play()
    except Exception:
        pygame.event.pump()
        sleep(2)
