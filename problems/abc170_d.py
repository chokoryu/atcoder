from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    multiples = [1] * (10 ** 6 + 1)

    bucket = Counter(A)
    res = 0

    for num in A:
        if bucket[num] == 1 and multiples[num] == 1:
            res += 1
        if multiples[num] == 1:
            for i in range(num, 10**6+1, num):
                multiples[i] = 0
    
    print(res)

if __name__ == '__main__':
    main()