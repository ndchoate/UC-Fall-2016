from hw04 import *

def main():
    s = make_s()
    lst = [next(s) for _ in range(20)]
    print(lst)

if __name__ == '__main__':
    main()