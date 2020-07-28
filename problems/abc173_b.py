from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    res = ['AC','WA','TLE','RE']

    for ans in res:
        print(ans + ' x ' + str(S.count(ans)))

if __name__ == '__main__':
    main()