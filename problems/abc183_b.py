from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    Sx, Sy, Gx, Gy = map(int, input().split())

    x = (Gy * Sx + Sy * Gx) / (Gy + Sy)
    print(x)

if __name__ == '__main__':
    main()