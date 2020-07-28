from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, B, C, D = map(int, input().split())

    if B / A == D / C:
        print('DRAW')
    else:
        print('TAKAHASHI') if B / A > D / C else print('AOKI')

if __name__ == '__main__':
    main()