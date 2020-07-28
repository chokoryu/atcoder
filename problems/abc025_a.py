from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    S = input()
    N = int(input())

    group = []

    for char1 in S:
        for char2 in S:
            group.append(char1+char2)
    
    group.sort()

    print(group[N-1])

if __name__ == '__main__':
    main()