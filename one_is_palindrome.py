#one line version of is_palindrome.py

def one_is_palindrome(string):
    if string == string[::-1]: return True
    else: return False

if __name__ == '__main__':
    if one_is_palindrome("racecar") == True: print("true")
    else: print("false")