# ABC159 D

import math

def main():
    n = int(input())
    A = list(map(int, input().split()))

    for i in range(n):
        newList = A[:i] + A[i+1:n]
        result = 0

        elements = set(newList)

        if elements == newList:
            print(result)
            continue
        elif len(elements) == 1:
            print(combinations_count(len(newList), 2))
            continue

        for elem in elements:
            result += combinations_count(newList.count(elem), 2)
        
        print(result)

def combinations_count(n, r):
    if n - r < 0:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if __name__ == '__main__':
    main()