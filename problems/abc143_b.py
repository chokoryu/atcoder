from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    d = list(map(int, input().split()))

    res = 0

    for i in range(N-1):
        for j in range(i+1, N):
            res += d[i] * d[j]

    print(res)

if __name__ == '__main__':
    main()