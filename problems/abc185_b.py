from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, M, T = map(int, input().split())

    time = 0
    res = N

    for _ in range(M):
        A, B = map(int, input().split())
        res = res - (A - time)

        if res <= 0:
            break

        res = min(N, res + (B - A))
        time = B

    res -= (T - time)

    print('Yes') if res > 0 else print('No')

if __name__ == '__main__':
    main()