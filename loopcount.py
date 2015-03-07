#loop and count ch 8 ex 5/6
#2014 brupoon

#from newfind.py
def find(string, letter, start = 0):
    """Find function using a string and a search letter.
    [Optionally] can specify start index as well."""
    index = start
    while index < len(string):
        if string[index] == letter:
            return index
        index = index + 1
    return -1

#this file's work
def count(word, letter):
    count = 0
    for increment in word:
        if increment == letter:
            count = count + 1
    print(count)
"""    
def countv2(word, letter):
    count = 0
    start = 0
    while True:
        if find(word, letter, start) != -1:
            count = count + 1
            start = find(word, letter, start)
        if find(word, letter) == -1:
            break
    print(count)
""" #Didn't work
if __name__ == '__main__':
    countv("banana", "a")