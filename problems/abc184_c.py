import math
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    manhattan = abs(r1 - r2) + abs(c1 - c2)

    if r1 == r2 and c1 == c2:
        print(0)
    elif (r1 + c1 == r2 + c2) or (r1 - c1 == r2 - c2) or (manhattan <= 3):
        print(1)
    elif abs(abs(c1 - c2) - abs(r1 - r2)) > 3:
        if manhattan % 2:
            print(3)
        else:
            print(2)
    else:
        print(2)

if __name__ == '__main__':
    main()