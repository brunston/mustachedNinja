#Gadsby -- Ch 10 Ex 2
#brupoon 2014
import os
def has_no_e(word):
    for letter in range(0,len(word)):
        ordval = ord(word[letter])
        if ordval == 101:
            return False
    return True

def main():
    """Adapted from wordsgreater20.py"""
    fin = open('words.txt')
    output = open('output.txt', 'w')
    without_e = 0
    total = 0
    
    for line in fin:
        word = line.strip()
        total = total + 1
        if has_no_e(word) == True:
            output.write(word + "\n")
            without_e = without_e + 1
    
    percentage = without_e / total * 100
    str_percentage = str(percentage)
    print("Output has occured at output.txt. Percentage without E: "
          + str_percentage + "%")
    print("Words without e: " + str(without_e))
    print("Words total: " + str(total))

if __name__ == '__main__':
    main()