"""
eval_loop
(c) @elegantonyx
Ch. 7, Ex 4
"""

from math import sqrt

def eval_loop():
    while True:
        user_inp = input("value?> ")
        if user_inp.lower() == "done":
            break
        print(eval(user_inp))

if __name__ == '__main__':
    eval_loop()

#work in progress, i guess.