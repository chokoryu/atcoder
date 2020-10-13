from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    P = list(map(int, input().split()))

    minValue = 0
    bucket = [0] * 200001

    for p in P:
         bucket[p] += 1
         if p == minValue:
              while bucket[minValue] != 0:
                   minValue += 1
         print(minValue)

if __name__ == '__main__':
    main()