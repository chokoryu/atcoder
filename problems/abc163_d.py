# ABC163 D

import math

def main():
    
    print(combinations_count(4,0))

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if __name__ == '__main__':
    main()