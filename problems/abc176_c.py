from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    A = list(map(int, input().split()))

    res = 0

    for i in range(1, N):
        if A[i] < A[i-1]:
            res += A[i-1] - A[i]
            A[i] = A[i-1]
    
    print(res)

if __name__ == '__main__':
    main()