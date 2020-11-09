from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
     A,B = map(int, input().split())

     follow_max = 2 * A + 100
     res = max(0, follow_max - B)

     print(res)

if __name__ == '__main__':
     main()