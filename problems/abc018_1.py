from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    scores = [int(input()) for _ in range(3)]

    sorted_scores = sorted(scores, reverse=True)

    for score in scores:
        print(sorted_scores.index(score) + 1)

if __name__ == '__main__':
    main()