from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertoolas import accumulate, product, permutations, combinations

def main():
    N, K = map(int, input().split())

    res = 0aaaa

    for i in range(1, N+1):
        tmp = 1 / N
        now = i

        while(now<K):
            now *= 2
            tmp /= 2

        res += tmp

    print(res)

if __name__ == '__main__':
    main()