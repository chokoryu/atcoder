from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, S, T = map(int, input().split())
    weights = list(accumulate([int(input()) for _ in range(N)]))

    res = 0

    for i in range(0, N):
        if S <= weights[i] <= T:
            res += 1
    
    print(res)

if __name__ == '__main__':
    main()