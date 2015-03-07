#Chapter 5 Exercise 2, do_n
# CC-BY-SA 4.0, bpoon 2014

def do_n(funct,n):
    if n <= 0:
        return
    funct()
    do_n(funct,n-1)

def pr_lol():
    print "lol"

if __name__ == '__main__':
    do_n(do_n_funct, wtf)