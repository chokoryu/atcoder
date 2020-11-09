from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
     N = int(input())
     A = list(map(int, input().split()))

     total_sum = [A[0]]
     max_coordinate = []

     for i in range(1, N):
          total_sum.append(total_sum[i-1]+A[i])

     prev_point = 0

     for i in range(0,N):
          max_point = max(prev_point, prev_point+A[i])
          max_coordinate.append(max_point)
          prev_point += A[i]

     print(max_coordinate)


if __name__ == '__main__':
     main()