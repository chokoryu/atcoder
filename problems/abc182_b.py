from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
     N = int(input())
     A = list(map(int, input().split()))

     k_max = max(A)
     max_count = 0
     res = 0

     for i in range(2, k_max+1):
          tmp_count = 0
          for j in range(N):
               if A[j] % i == 0:
                    tmp_count += 1
               if tmp_count > max_count:
                    max_count = tmp_count
                    res = i

     print(res)

if __name__ == '__main__':
     main()