#-------------------------------------------------------------------------------
# Name:        mypolygon4-7
# Author:      B Poon
# Created:     23 12 2013
# Copyright:   (c) B Poon 2013
# Licence:     gnu lgplv3
#-------------------------------------------------------------------------------

from TurtleWorld import *
from math import *

def square(turt, leng):
    """Prints a square using turtle turt and side length leng."""
    print(turt)
    for i in range(4):
        fd(turt, leng)
        lt(turt)

def polyline(turt, n, length, angle):
    """Draws n line segments with the given length and angle (in degrees)
    between them. t is a turtle.
    """
    for i in range(n):
        fd(turt, length)
        lt(turt, length)

def polygon(turt, leng, n):
    """Uses polyline to create a closed polygon with n sides."""
    angle = 360 / n
    polyline(turt, n, leng, angle)

def circle(turt, radius):
    """Specialized polygon emulating a circle."""
    arc(turt, radius, 360)

def arc(turt, radius, angle):
    """Creates an arc."""
    pieces = 2*pi*radius*angle/360
    n = int(pieces / 3) + 1
    stepLength = pieces / n
    stepAngle = float(angle) / n

    # code from thinkpython reducing the error caused by linear approx. of arc
    lt(turt, stepAngle/2)
    polyline(turt,n,stepLength,stepAngle)
    rt(turt, stepAngle/2)

def test():
    world = TurtleWorld()
    bob = Turtle()
    bob.delay= 0.01
    arc(bob, 100, 120)
    wait_for_user()

if __name__ == '__main__':
    test()
