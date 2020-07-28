from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cumsumA = [0] + list(accumulate(A))
    cumsumB = [0] + list(accumulate(B))

    res = 0

    for i in range(N+1):
        if i == 0:
            for j in range(M, -1, -1):
                if cumsumB[j] <= K:
                    max_j = j
                    res = max(res, i + j)
                    break
        else:
            for j in range(max_j, -1, -1):
                time = cumsumA[i] + cumsumB[j]
                if  time <= K:
                    max_j = j
                    res = max(res, i + j)
                    break
    
    print(res)

if __name__ == '__main__':
    main()