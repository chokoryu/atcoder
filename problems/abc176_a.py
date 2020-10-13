from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, X, T = map(int, input().split())

    if N % X == 0:
        print((N // X) * T)
    else:
        print((N // X + 1) * T)

if __name__ == '__main__':
    main()