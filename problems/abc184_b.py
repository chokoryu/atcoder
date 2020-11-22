from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, X = map(int, input().split())
    S = input()

    for i in range(N):
        if S[i] == 'x' and X != 0:
            X -= 1
        elif S[i] == 'o':
            X += 1

    print(X)

if __name__ == '__main__':
    main()