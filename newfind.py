#FIND
# @brupoon 2014

def find(string, letter, start = 0):
    """Find function using a string and a search letter.
    [Optionally] can specify start index as well."""
    index = start
    while index < len(string):
        if string[index] == letter:
            return index
        index = index + 1
    return -1

if __name__ == '__main__':
    number = find("banana", "n", 3)
    print(number)