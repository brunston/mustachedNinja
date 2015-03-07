#print_backwards
# @brupoon 2014

def print_backwards(string):
    index = len(string)
    while index > 0:
        letter = string[index-1]
        print(letter)
        index = index - 1

if __name__ == '__main__':
    print_backwards("antidisestablishmentarianism")