from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    A = list(map(int, input().split()))

    min = 10 << 63
    res = 0

    for i in range(N):
        res += A[i]
        if min > A[i]:
            min = A[i]
    
    print(res - min)

if __name__ == '__main__':
    main()