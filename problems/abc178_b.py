from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    a, b, c, d = map(int, input().split())

    res = [a*c, a*d, b*c, b*d]

    print(max(res))

if __name__ == '__main__':
    main()