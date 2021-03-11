from math import *
from cmath import *
from random import *
from matplotlib.pyplot import *
from helperModules import *


def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


formula = input("Enter Formula to calculate Y: ")
c = int(input("Range of Returned Numbers: "))
v = float(input("in steps of: "))
returns = rangeNew(-c, c, v)  # [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

x = -15.0

xL, yL = [], []

while x <= 15:
    y = eval(formula)
    try:
        if x in returns:
            print(x, ":", y)
    except TypeError:
        if x == returns:
            print(x, ":", y)
    x += 0.25
    xL.append(x)
    yL.append(y)

axis([-8, 8, -12, 12])
title(formula)
plot(xL, yL)
grid()
show()
