from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())

    res = 0
    odd_flag = False

    if N % 2:
        odd_flag = True
        N -= 1
        res += N // 2
    else:
        res += N // 2
    
    if odd_flag:
        print(res + 1)
        print(1)
    else:
        print(res)
    for i in range(res):
        print(2)

if __name__ == '__main__':
    main()