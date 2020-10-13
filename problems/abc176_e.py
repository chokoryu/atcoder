from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    H, W, M = map(int, input().split())
    bombs = list(list(map(int, input().split())) for _ in range(M))

    hBucket = [0] * H

    for bomb in bombs:
        hBucket[bomb[0]-1] += 1
    
    rowList = []
    maxBombH = 0

    for i in range(len(hBucket)):
        if hBucket[i] > maxBombH:
            maxBombH = hBucket[i]
            rowList = [i]
        elif hBucket[i] == maxBombH:
            rowList.append(i)
    
    maxBombW = []

    for row in rowList:
        wBucket = [0] * W
        for bomb in bombs:
            if bomb[0] != row + 1:
                wBucket[bomb[1]-1] += 1
    
        maxBombNum = max(wBucket)
        maxBombW.append(maxBombNum)
    
    print(maxBombH + max(maxBombW))

if __name__ == '__main__':
    main()