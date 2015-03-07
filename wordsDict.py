#Chapter 11, Exercise 1
#bpoon

def main():
    words = open('words.txt')
    wordDict = dict()
    for i in words:
        word = i.strip()
        wordDict[word] = "yes"

def uInput():
    uInput = input("word?")
    if uInput in wordDict:
        print("In dictionary.")
    else:
        print("Not in dictionary.")
    uInput()
if __name__ == '__main__':
    main()