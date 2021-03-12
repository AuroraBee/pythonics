from math import *
import math


def scaleTo(num, rangeKnown, scale=255.0):
    if scale == rangeKnown:
        return num
    x = num * (scale / rangeKnown)
    if x > scale:
        x = scale
    return x


def rangeNew(i, o=0, p: float = 1):
    if o == 0:
        o = i - 2
    if o <= i:
        i = 0
    l = []
    while i <= o + p:
        l.append(i)
        i += p
    return l
