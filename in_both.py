#in_both (ch 8.9)
#brupoon 2014

def in_both(word1, word2):
    """Prints all letters in word1 that appear in word2"""
    for letter in word1:
        if letter in word2:
            print(letter)

if __name__ == '__main__':
    in_both("apple","orange")
    
