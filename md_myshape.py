# creates a module
# myshape.py

import turtle as t

def 정사각형(size) :
    for i in range(4) :
        t.forward(size)
        t.left(90)
    return 0

def 정삼각형(size) :
    for i in range(3) :
        t.forward(size)
        t.left(360/3)
    return 0

def 정원그리기(size) :
    t.circle(size)
    return 0

    