#ch 10 ex 3, avoids
#2014 brupoon

def letter_check(word,check_ord):
    """
    Checks for a letter with the ordval stored in check_ord within word.
    Returns false if word contains that letter.
    Returns true if word doesn't contain that letter.
    """
    for letter in range(0,len(word)):
        ordval = ord(word[letter])
        if ordval == check_ord:
            return False
    return True

def avoids(word, forbstring):
    """
    Boolean function which returns True if word does not contain any characters
    from forbstring
    """
    betrayal_tracker = True
    toggle = False
    while toggle == False:
        for letter in range(0, len(forbstring)):
            letter_to_compare = forbstring[letter]
            letter_to_compare_ord = ord(letter_to_compare)
            if letter_check(word, letter_to_compare_ord) == False:
                betrayal_tracker == False
                break
        toggle = True
    return betrayal_tracker

def avoids_answer(word, forbstring):
    """that moment when your code is far too complicated and the answer
    is super simple...This follows the same structure as letter_check"""
    #alternate implementation, not mine
    
    for letter in word:
        if letter in forbstring:
            return False
    return True
    
def uses_only(word, only):
    """
    Returns True if word only uses letters in only
    """
    
    for letter in word:
        if letter not in only:
            return False
    return True

def uses_all(word, required):
    """
    Returns True if word uses all letters within required
    """
    
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_all_alt(word, required):
    #alternate implementation, not mine
    return uses_only(required, word)

def is_abecedarian(word):
    """
    Returns True if letters within word are arranged alphabetically.
    """
    counter = 0
    for letter in word:
        counter = counter + 1
        if counter == 1:
            pass
        elif ord(letter) < ord(word[counter-2]):
            return False
    return True
    
def recursiveAbecedarian(word):
    """
    Returns True if letters within word are arranged alphabetically.
    This function does this recursively.
    """
    #alternate implementation, not mine
    
    if len(word) <=1:
        return True
    if word[0] > word[1]:
        return False
    recursiveAbecedarian(word[1:])
    
def forAbecedarian(word):
    """
    Returns True if letters within word are arranged alphbetically.
    This function does this recursively.
    """
    #alternate implementation, not mine
    
    previous = word[0]
    for i in word:
        if c < previous:
            return False
        previous = c
    return True
    


if __name__ == '__main__':
    print(is_abecedarian("abecd"))