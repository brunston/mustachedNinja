#is_reverse (ch 8.11)
#brupoon 2014

def is_reverse(word1, word2):
    """Determines if word1 and word2 are reverses of each other"""
    
    if len(word1) != len(word2): #guardian check
        return False
    i = 0
    j = len(word2)-1 #-1 to account for how indexing works
    
    while j >= 0: #has to be >= so the last set of letters are checked
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    
    return True