from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    S = input()

    if S[-1] == 's':
        print(S + 'es')
    else:
        print(S + 's')

if __name__ == '__main__':
    main()