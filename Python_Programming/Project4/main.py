from hw04 import *

def main():
    twos = scale(naturals(), 2)
    threes = scale(naturals(), 3)
    fives = scale(naturals(), 5)
    m = merge(threes, fives)
    lst = [next(m) for _ in range(10)]
    print(lst)

if __name__ == '__main__':
    main()