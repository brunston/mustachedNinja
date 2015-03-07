"""
bplib3 2014, python 3.3
brupoon 2014
cite as so: [programname] uses bplib3py
use: place bplib3.py in same directory, type 'import bplib3' to import module
"""

def ri_int(text):
    """converts input to int"""
    foo = input(text)
    fooint = int(foo)
    return fooint

def ri_float(text):
    """converts input to float"""
    foo = input(foo)
    foofloat = float(foo)
    return foofloat

def absg(a,b):
    """Ghetto abs() which doesn't throw weird errors"""
    difference = a - b
    if difference < 0:
        difference = -difference
    return difference

def factorial(n):
    """recursive factorial implementation. Calculates n!""" 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sqrt_aprx(a):
    """Approximates the square root of input a to accuracy of 0.000001"""
    x = a/2
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < 0.000001:
            break
        x = y
        
    return x

def rotate_word(string, rot_value):
    """
    Rotates word by rotation value specified, as in a Caesar cipher.
    
    string: alphabetic word, not modified by spaces or dashes.
    rot_value: value which the rotation occurs around. Must be an int.
    """
    
    string_l = string.lower() #simplifies string
    string_rot = ""
    
    for i in range(0,len(string_l)):
        old_char_ord = ord(string_l[i])-97 #converting to alpha value
        new_char_ord = (old_char_ord + rot_value) % 26 + 97
        #above line transposes mod 26 and deconverts back to ord value
        new_char = chr(new_char_ord)
        string_rot = string_rot + new_char #concatenates
   
    return string_rot

def rot_tester():
    """
    Gets string and rotation value from user while checking for int.
    Used in parallel with rotate_word
    """
    
    user_string = input("Alphabetic string> ")
    value = input("Rotation value> ")
    tester = True
    while tester == True:
        try:
            int_value = int(value)
            tester = False
        except ValueError:
            value = input("Requires integer value. Try again> ")
    print(rotate_word(user_string, int_value))

def recurse(toggle = False):
    """
    Foolproof Recursion. toggle (set true/false) sets infinte recursion.
    """
    try:
        recurse()
    except RuntimeError:
        recurse()
