import os
import random

def getDirtyLine():
    f = open('dirtyLines.txt', 'r')
    l = f.readline()
    a = l.split("******")
    a_len = len(a)
    print(a_len)
    r_int = random.randint(0, a_len - 1)
    print(a[r_int])
    return a[r_int]

getDirtyLine()

