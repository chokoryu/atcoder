from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, K = map(int, input().split())

    ans = K

    for _ in range(N-1):
        ans = ans * (K - 1)

    print(ans)

if __name__ == '__main__':
    main()