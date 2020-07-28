from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())

    if N == 100:
        print('Perfect')
    elif N >= 90:
        print('Great')
    elif N >= 60:
        print('Good')
    else:
        print('Bad')

if __name__ == '__main__':
    main()