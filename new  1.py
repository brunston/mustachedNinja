#Chapter 11, Exercise 1
#bpoon

def main():
    words = open("words.txt")
    wordDict = dict()
    for i in words:
        word = i.strip()
        wordDict[word] = "yes"