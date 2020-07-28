# ABC159 A

import math

def main():
    n, m = map(int, input().split())
    
    if n >= 2 and m >= 2:
        even = math.factorial(n) // (math.factorial(n-2) * math.factorial(2))
        odd = math.factorial(m) // (math.factorial(m-2) * math.factorial(2))
    elif m >= 2:
        even = 0
        odd = math.factorial(m) // (math.factorial(m-2) * math.factorial(2))
    elif n >= 2:
        even = math.factorial(n) // (math.factorial(n-2) * math.factorial(2))
        odd = 0
    else:
        even = 0
        odd = 0

    print(even + odd)

if __name__ == '__main__':
    main()