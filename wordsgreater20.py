#Ch 10 ex 1
#prints from words.txt with words greater than 20 characters.
#brupoon 2014

def main():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
    
if __name__ == '__main__':
    main()