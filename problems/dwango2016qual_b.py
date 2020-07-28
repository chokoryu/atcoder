from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())
    K = list(map(int, input().split()))
    
    res = []

    for i in range(N-1):
        if i == 0:
            res.append(1)
        else:
            if K[i] >= K[i-1]:
                res.append(K[i-1])
            else:
                res[i-1] = K[i-1]
                res.append(K[i])
    
    res.append(K[-1])

    print(' '.join(list(map(str, res))))
    

if __name__ == '__main__':
    main()