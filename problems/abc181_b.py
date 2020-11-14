from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    res = 0

    for i in range(N):
        A, B = map(int, input().split())
        n = B - A + 1
        res += n * (2*A + (n-1)) / 2

    print(int(res))

if __name__ == '__main__':
    main()