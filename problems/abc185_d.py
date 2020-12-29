import math
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    stamps = [0] * N
    for i in range(M):
        stamps[A[i]-1] = 1
    white_list = []
    white_count = 0
    k = N
    res = 0

    for i in range(N):
        if stamps[i] == 1:
            if white_count != 0:
                white_list.append(white_count)
                if white_count < k:
                    k = white_count
                white_count = 0
        else:
            white_count += 1

        if (i == (N - 1)) and (white_count != 0):
            white_list.append(white_count)
            if white_count < k:
                k = white_count

    for i in range(len(white_list)):
        res += math.ceil(white_list[i] / k)

    print(res)

if __name__ == '__main__':
    main()