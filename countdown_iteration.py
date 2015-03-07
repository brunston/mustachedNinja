#countdown, using iteration

def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("blastoff!")
    
if __name__ == '__main__':
    countdown(5)