import math
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    L = list(map(int, input().split()))

    res = 0

    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if (L[i] == L[j]) or (L[j] == L[k]) or (L[i] == L[k]):
                    continue
                else:
                    side_i = L[i] - L[j] - L[k]
                    side_j = L[j] - L[i] - L[k]
                    side_k = L[k] - L[i] - L[j]

                    if (side_i < 0) and (side_j < 0) and (side_k < 0):
                        res += 1

    print(res)

if __name__ == '__main__':
    main()