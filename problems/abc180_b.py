from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import math

def main():
    N = int(input())
    x = list(map(int, input().split()))

    print(sum(list(abs(i) for i in x)))
    print(math.sqrt(sum(list(abs(i)**2 for i in x))))
    print(max(list(abs(i) for i in x)))

if __name__ == '__main__':
    main()