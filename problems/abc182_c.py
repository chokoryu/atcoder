from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
     N = input()

     if int(N) % 3 == 0:
          print(0)
     else:
          bits = 2 ** len(N)
          res = len(N)
          for i in range(1, bits):
               sum = 0
               count = 0
               for j in range(len(N)):
                    if (i >> j) & 1:
                         sum += int(N[j])
                         count += 1
               if sum % 3 == 0 and len(N)-count < res:
                    res = len(N) -count

          print(-1) if res == len(N) else print(res)

if __name__ == '__main__':
     main()