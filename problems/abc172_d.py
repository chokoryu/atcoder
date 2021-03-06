from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())

    res = 0

    for i in range(1, N+1):
        n = N // i
        res += n * (2 * i + (n - 1) * i) // 2
    
    print(res)

if __name__ == '__main__':
    main()