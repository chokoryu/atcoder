from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, D = map(int, input().split())

    res1 = (A + 1) * D
    res2 = A * (D + 1)

    if res1 >= res2:
        print(res1)
    else:
        print(res2)

if __name__ == '__main__':
    main()