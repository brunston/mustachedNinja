# histogram
# brupoon

def histogram(str):
    d = dict()
    for char in str:
        d[char] = 1 + d.get(char, 0)
    print(d)
    
def print_histogram(h):
    for c in h:
        print c, h[c]

if __name__ == '__main__':
    histogram("abcdefghijklmnopqrrr")