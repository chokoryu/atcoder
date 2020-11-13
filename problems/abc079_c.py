import sys
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, B, C, D = tuple(map(int, input()))

    ops = ['+', '-']

    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                if op1 == '+':
                    tmp1 = A + B
                else:
                    tmp1 = A - B

                if op2 == '+':
                    tmp2 = tmp1 + C
                else:
                    tmp2 = tmp1 - C

                if op3 == '+':
                    tmp3 = tmp2 + D
                else:
                    tmp3 = tmp2 - D

                if tmp3 == 7:
                    print(str(A)+op1+str(B)+op2+str(C)+op3+str(D)+'=7')
                    sys.exit()

if __name__ == '__main__':
    main()