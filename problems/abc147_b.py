from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    S = input()

    res = 0

    for i in range(len(S)//2):
        if S[i] != S[-1-i]:
            res += 1

    print(res)

if __name__ == '__main__':
    main()