#Ch 6 ex 5, Ackermann function
#brupoon 2014

def ack(m,n):
    """evaluated Ackermann's function on m and n, if n and m are
    non-negative integers"""
    if m == 0:
        return n+1
    if m > 0:
        if n == 0:
            return ack(m-1, 1)
        if n > 0:
            return ack(m-1, ack(m, n-1))
    if m < 0:
        print "Ackermann's function doesn't computer for negative ints"
        return None

if __name__ == '__main__':
    ack34 = ack(3,4)
    print ack34
    
