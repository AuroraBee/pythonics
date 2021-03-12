from kandinsky import *
import datetime


class Logger:
    def __init__(self, name="AntLog"):
        self.file = open(name + '-{date:%Y-%d-%m_%H-%M-%S}.log'.format(date=datetime.datetime.now()), "w")

    def debug(self, text):
        self.file.write("[DEBUG] " + text)

    def warn(self, text):
        self.file.write("[WARN] " + text)

    def error(self, text):
        self.file.write("[ERROR] " + text)


class Ant:
    def __init__(self, x, y, ruleBlack="right", ruleWhite="left", direction="down", log=Logger()):
        pygame.event.pump()
        self.log = log
        self.ruleBlack = ruleBlack
        self.ruleWhite = ruleWhite
        self.x = x
        self.y = y
        self.dir = direction
        self.dirlistClockwise = {
            "up": "right",
            "right": "down",
            "down": "left",
            "left": "up"
        }
        self.dirlistCounter = {
            "up": "left",
            "left": "down",
            "down": "right",
            "right": "up"
        }

    def invert(self):
        pygame.event.pump()
        pixel = get_pixel(self.x, self.y)
        if pixel == color(0, 0, 0):
            set_pixel(self.x, self.y, color(255, 255, 255))
            self.log.debug("Received WHITE at " + str(self.x) + " " + str(self.y) + "\n")
            return "white"
        else:
            set_pixel(self.x, self.y, color(0, 0, 0))
            self.log.debug("Received BLACK at " + str(self.x) + " " + str(self.y) + "\n")
            return "black"

    def move(self):
        pygame.event.pump()
        newDir = self.invert()
        dir = self.dir
        if newDir == "black":
            if self.ruleBlack == "left":
                self.dir = self.dirlistCounter[self.dir]
                self.log.debug("Direction changed to " + self.dirlistCounter[self.dir] + "\n")
            if self.ruleBlack == "right":
                self.dir = self.dirlistClockwise[self.dir]
                self.log.debug("Direction changed to " + self.dirlistClockwise[self.dir] + "\n")
        if newDir == "white":
            if self.ruleWhite == "left":
                self.dir = self.dirlistCounter[self.dir]
                self.log.debug("Direction changed to " + self.dirlistCounter[self.dir] + "\n")
            if self.ruleWhite == "right":
                self.log.debug("Direction changed to " + self.dirlistClockwise[self.dir] + "\n")
                self.dir = self.dirlistClockwise[self.dir]
        self.log.debug("Ant move starting" + "\n")
        if dir == "up":
            self.y -= 1
        if dir == "down":
            self.y += 1
        if dir == "left":
            self.x -= 1
        if dir == "right":
            self.x += 1
        self.log.debug("Ant moved successfully!" + "\n")


log = Logger()


def Antsy(y, log=Logger()):
    ant = Ant(160, 111+y, log=log)

    while 1:
        pygame.event.pump()
        try:
            ant.move()
        except Exception:
            file = open("log.txt", "a")
            file.write("\n Program Exited due to Exception... \n")
            break


for i in range(5):
    Antsy(i, log=log)
