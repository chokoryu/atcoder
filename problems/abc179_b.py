from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    same_count = 0
    yes_flag = False

    for _ in range(N):
        D1, D2 = map(int, input().split())

        if D1 == D2:
            same_count += 1
        else:
            same_count = 0

        if same_count == 3:
            yes_flag = True

    print('Yes') if yes_flag else print('No')

if __name__ == '__main__':
    main()