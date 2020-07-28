from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    Ng = [int(input()) for _ in range(3)]

    res = 'NO'

    for i in range(100):
        if N in Ng: break
        if N - 3 in Ng:
            if N - 2 in Ng:
                if N - 1 in Ng:
                    break
                else:
                    N -= 1
            else:
                N -= 2
        else:
            N -= 3
        
        if N <= 0:
            res = 'YES'
            break

    print(res)

if __name__ == '__main__':
    main()