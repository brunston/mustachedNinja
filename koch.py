#koch, create a Koch curve/snowflake, ch 5 ex 6
#CC-BY-SA 4.0, bpoon 2014

from swampy.TurtleWorld import *

def koch(t, length):
    """creates koch curve using turtle t and length length"""
    if length < 3:
        fd(t,length)
        return
    length3 = length/3.0
    koch(t,length3)
    lt(t,60)
    koch(t,length3)
    rt(t, 120)
    koch(t,length3)
    lt(t,60)
    koch(t,length3)

def snowflake(t, length):
    """creates koch snowflake using turtle t and length length"""
    for i in range(3):
        koch(t, length)
        rt(t,120)
        
        
if __name__ == '__main__':
    """Runs if koch.py is invoked as primary file"""
    world = TurtleWorld()
    foo = Turtle()
    foo.x = -100
    foo.y = 100
    foo.redraw()
    snowflake(foo,300)
    wait_for_user()
