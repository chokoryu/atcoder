import math
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, B = map(int, input().split())

    if B == 1:
        print(0)
    elif B > A:
        print(math.ceil((B - A) / (A - 1)) + 1)
    else:
        print(1)

if __name__ == '__main__':
    main()