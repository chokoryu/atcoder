from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    scores = [list(map(int, input().split())) for _ in range(3)]

    res = 0

    for score in scores:
        res += score[0] * score[1] * 0.1
    
    print(int(res))

if __name__ == '__main__':
    main()