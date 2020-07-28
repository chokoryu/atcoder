from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    W, H = map(int, input().split())

    if W / 16 == H / 9:
        print('16:9')
    else:
        print('4:3')

if __name__ == '__main__':
    main()