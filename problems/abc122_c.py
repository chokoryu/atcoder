from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, Q = map(int, input().split())
    S = input()

    index_AC = [0] * N

    for i in range(1, N):
        if S[i-1] == 'A' and S[i] == 'C':
            index_AC[i] = index_AC[i-1] + 1
        else:
            index_AC[i] = index_AC[i-1]

    for _ in range(Q):
        l, r = map(int, input().split())

        res = index_AC[r-1] - index_AC[l-1]

        print(res)

if __name__ == '__main__':
    main()