from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, B, C, K = map(int, input().split())
    S, T = map(int, input().split())

    if S + T >= K:
        print(S * (A - C) + T * (B - C))
    else:
        print(S * A + T * B)

if __name__ == '__main__':
    main()