from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A = int(input())

    print(A//2 * (A//2 + 1)) if A%2 else print((A//2) ** 2)

if __name__ == '__main__':
    main()