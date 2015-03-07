#check_fermat (Ch 5 Ex 3)
#CC-BY-SA 4.0, bpoon 2014

def check_fermat(a,b,c,n):
    """Check's Fermat's Last Theorem (no ints a,b,c such that a^n + b^n = c^n for vals n >2)"""
    if n>2:
        if (a**n + b**n) == (c**n):
            print "Holy smokes, Fermat was wrong!"
        else:
            print "No, that doesn't work."
    else:
        print "This case isn't in the scope of Fermat's Last Theorem."
        
        
if __name__ == '__main__':
    a = raw_input("a: ")
    a_int = int(a)
    b = raw_input("b: ")
    b_int = int(b)
    c = raw_input("c: ")
    c_int = int(c)
    n = raw_input("n: ")
    n_int = int(n)
    check_fermat(a_int, b_int, c_int, n_int)