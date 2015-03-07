#ch 6 ex 1, compare function
#cc-by-sa 4.0, bpoon 2014

def compare(x,y):
    """compares two numbers and returns 1 if x>y, 0 if x=y, and -1 if x<y"""
    if x>y:
        return 1
    if x == y:
        return 0
    if x<y:
        return -1
    return "wtf"
