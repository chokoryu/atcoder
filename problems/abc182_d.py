from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
     N = int(input())
     A = list(map(int, input().split()))

     total_sum = [i for i in accumulate(A)]
     total_sum = [i for i in accumulate(total_sum)]
     max_coordinate = []

     prev_point = 0
     max_point = 0

     for i in range(0,N):
          max_point = max(max_point, prev_point+A[i])
          max_coordinate.append(max_point)
          prev_point += A[i]

     res = max(total_sum[0], max_coordinate[0])

     for i in range(1, N):
          tmp = total_sum[i-1] + max_coordinate[i]
          if tmp > res:
               res = tmp

     print(res)

if __name__ == '__main__':
     main()