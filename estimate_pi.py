#estimate pi (ramanujan infinite series)
# @brupoon 2014
# estimate_pi uses bplib3py
from math import *
import bplib3

def factorial(n):
    """recursive factorial""" 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def estimate_pi():
    """Estimate of Pi from work by Ramanujan"""
    summed = 0
    k = 0
    while True:
        multiplier = (2*sqrt(2))/9801
        top = factorial(4*k)*(1103+26390*k)
        bottom = (factorial(k)**4)*396**(4*k)
        term = multiplier * (top/bottom)
        summed = summed + term
        if term > 1e-15: break
        k = k+1
    return 1/summed

if __name__ == '__main__':
    print("Estimate: ", estimate_pi())
    print("math.pi: ", pi)
    print("Difference: ", bplib3.absg(estimate_pi(),pi))