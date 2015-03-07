#simple rot13 script (ch 9, ex 12)
#brupoon 2014

def rotate_word(string, rot_value):
    """
    Rotates word by rotation value specified, as in a Caesar cipher.
    
    string: alphabetic word, not modified by spaces or dashes.
    rot_value: value which the rotation occurs around. Must be an int.
    """
    
    string_l = string.lower() #simplifies string
    string_rot = ""
    
    for i in range(0,len(string_l)):
        old_char_ord = ord(string_l[i])-97 #converting to alpha value
        new_char_ord = (old_char_ord + rot_value) % 26 + 97
        #above line transposes mod 26 and deconverts back to ord value
        new_char = chr(new_char_ord)
        string_rot = string_rot + new_char #concatenates
   
    return string_rot

def tester():
    """
    Gets string and rotation value from user while checking for int.
    """
    
    user_string = input("Alphabetic string> ")
    value = input("Rotation value> ")
    tester = True
    while tester == True:
        try:
            int_value = int(value)
            tester = False
        except ValueError:
            value = input("Requires integer value. Try again> ")
    print(rotate_word(user_string, int_value))

if __name__ == '__main__':
    tester()