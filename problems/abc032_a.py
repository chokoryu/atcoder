from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    a = int(input())
    b = int(input())
    n = int(input())

    while True:
        if n % a == 0 and n % b == 0:
            break
        else:
            n += 1
    
    print(n)

if __name__ == '__main__':
    main()