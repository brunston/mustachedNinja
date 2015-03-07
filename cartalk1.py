#Cartalk Puzzler 1 (Ch 9 ex 7)
#2014 brupoon

def threeConsecutive(word):
    """
    Returns False if $word doesn't contain three sets of double consecutive
    words, and returns True if $word does. Also prints if it does.
    """
    
    if len(word) < 6:
        return False
    
    previous = word[0:2]
    for letter in previous:
        if previous[letter] == previous[letter+1]:
    
if __name__ == '__main__':
    threeConsecutive("abcdef")