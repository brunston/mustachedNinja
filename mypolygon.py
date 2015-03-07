#-------------------------------------------------------------------------------
# Name:        mypolygon
# Author:      B Poon
# Created:     23 12 2013
# Copyright:   (c) B Poon 2013
# Licence:     CCBYSA4.0
#-------------------------------------------------------------------------------

from TurtleWorld import *
from math import *

def square(turt, leng):
    print(turt)
    for i in range(4):
        fd(turt, leng)
        lt(turt)

def polygon(turt, leng, n):
    print(turt)
    for i in range(n):
        fd(turt, leng)
        lt(turt, 360/n)

def circle(turt, radius):
    pieces = (2*pi*radius)/360
    polygon(turt, pieces, 360)

def arc(turt, radius, angle):
    pieces = 2*pi*radius*angle/360
    n = int(pieces / 3) + 1
    stepLength = pieces / n
    stepAngle = float(angle) / n
    for i in range(n):
        fd(turt, stepLength)
        lt(turt, stepAngle)

def main():
    world = TurtleWorld()
    bob = Turtle()
    bob.delay= 0.01
    arc(bob, 100, 120)
    wait_for_user()

if __name__ == '__main__':
    main()
