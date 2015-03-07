#Chapter 9, Exercise 11...any_lowercase tests

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

if __name__ == '__main__':
    if any_lowercase2("test") == True: print("all lower: true")
    else: print("all lower: false")
    if any_lowercase2("Test") == True: print("firstupper: true")
    else: print("firstupper: false")
    if any_lowercase2("tEst") == True: print("middleupper: true")
    else: print("middleupper: false")
    if any_lowercase2("TEST") == True: print("all upper: true")
    else: print("all upper: false")