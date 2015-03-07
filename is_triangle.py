# Ch 5 Ex 4 Triangle Problem
#CC-BY-SA 4.0, bpoon 2014
#uses bplibpy
from bplib import ri_int
def is_triangle(a, b, c):
    """checks all values of a, b, c to see if valid triangle is possible"""
    if a + b >= c:
        if b +  c >= a:
            if c + a >= b:
                print "Yes"
            else:
                print "No"
        else:
            print "No"
    else:
        print "No"

def prompter():
    """prompter asks for three values, converts to int, and performs is_triangle"""
    a = raw_input("side a: ")
    b = raw_input("side b: ")
    c = raw_input("side c: ")
    a_int = int(a)
    b_int = int(b)
    c_int = int(c)
    is_triangle(a_int,b_int,c_int)

def prompterbplib():
    """prompterbplib uses ri_int from bplibpy and performs is_triangle"""
    a = ri_int("int vals for side a: ")
    b = ri_int("int vals for side b: ")
    c = ri_int("int vals for side c: ")
    is_triangle(a,b,c)

if __name__ == '__main__':
    prompterbplib()