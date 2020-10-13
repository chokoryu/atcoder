from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())

    k = N // 2 if N % 2 else int(N / 2 - 1)
    res = N // 2

    for i in range(1, k+1):
        res += (N - 1) // i

    print(res)

if __name__ == '__main__':
    main()