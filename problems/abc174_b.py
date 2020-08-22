from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, D = map(int, input().split())
    
    res = 0

    for i in range(N):
        x, y = map(int, input().split())
        dist = (x**2 + y**2)**0.5

        if dist <= D:
            res += 1
    
    print(res)

if __name__ == '__main__':
    main()