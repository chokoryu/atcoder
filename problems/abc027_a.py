from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    l1, l2, l3 = map(int, input().split())

    if l1 == l2:
        print(l3)
    elif l1 == l3:
        print(l2)
    else:
        print(l1)

if __name__ == '__main__':
    main()