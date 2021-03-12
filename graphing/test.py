from math import *
from cmath import *
from random import *
from matplotlib.pyplot import *

graphs = [
    [3, -20, 2, -2],
    [-5, 10, 2, 1],
    [1 / 3, -10, 2, 2],
    [1 / 4, 20, 2, -3]
]


def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


def plotter(m, n, b, v):
    n = 0
    if m == 0:
        m = 1
    if b == 0:
        b = 2
    formula = "m * ( x - n ) ** b + v"
    x = -30.0

    xL, yL = [], []

    while x <= 30:
        x += 0.5
        print(eval(formula))
        y = eval(formula)
        xL.append(x)
        yL.append(y)
    plot(xL, yL)


for vals in graphs:
    plotter(vals[0], vals[1], vals[2], vals[3])

axis([-40, 40, -30, 30])
grid()
show()
