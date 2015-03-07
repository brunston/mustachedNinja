#practicing incremental development, ch 6 ex 2
#cc-by-sa 4.0, bpoon 2014
import math
def hypotenuse(x,y):
    """calculates hypotenuse of right-angle triangle formed by legs with length
    x and y"""
    squaredx = x**2
    squaredy = y**2
    result_squared = squaredx + squaredy
    result = math.sqrt(result_squared)
    return result

def hypotenuse_compact(x,y):
    """taking the incrementally developed and shortening it"""
    return math.sqrt(x**2 + y**2)

if __name__ == '__main__':
    hyp = hypotenuse_compact(3,4)
    print hyp