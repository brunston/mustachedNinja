#is_between ch 6 ex 3
#cc-by-sa 4.0, bpoon 2014

def is_between(x,y,z):
    """checks to see if x<=y<=z is true and returns as bool."""
    if x <= y <= z:
        return True
    else:
        return False

if __name__ == '__main__':
    if is_between(3,4,5):
        print "yes"
    else:
        print "no"