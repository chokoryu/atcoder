from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    H, W = map(int, input().split())
    res = 0
    S = []

    for _ in range(H):
         tmp = list(input())
         S.append(tmp)
     
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                try:
                    if S[i][j+1] == '.':
                        res += 1
                except IndexError:
                    pass
                try:
                    if S[i+1][j] == '.':
                        res += 1
                except IndexError:
                    pass

    print(res)


if __name__ == '__main__':
    main()