# Panasonic2020 C

import math

def main():
    a, b, c = map(int, input().split())

    if 4*a*b < (c-a-b)**2 and c-a-b > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()