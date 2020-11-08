from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    S = input()

    res = 0
    tmp = 0

    for weather in S:
        if weather == 'R':
            tmp += 1
            if tmp > res:
                res = tmp
        else:
            tmp = 0

    print(res)

if __name__ == '__main__':
    main()