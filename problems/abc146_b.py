from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    S = input()

    res = []

    for char in S:
        tmp = ord(char)
        tmp += N

        if tmp > 90:
            tmp -= 26

        res.append(chr(tmp))

    print(''.join(res))

if __name__ == '__main__':
    main()