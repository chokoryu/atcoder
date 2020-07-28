from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    S = input().split('+')

    res = 0

    for term in S:
        if '*' not in term and term != '0':
            res += 1
        else:
            if '0' not in term:
                res += 1
    
    print(res)

if __name__ == '__main__':
    main()