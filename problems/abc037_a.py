from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, B, C = map(int, input().split())

    res = 0

    for i in range(1000000):
        if i * A > C:
            break
        else:
            j = (C - i * A) // B
            if i * A + j * B <= C:
                res = max(res, i + j)
            else:
                continue
    
    print(res)

if __name__ == '__main__':
    main()