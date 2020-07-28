from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]

    res = 0

    for h in list(product([0, 1], repeat=H)):
        for w in list(product([0, 1], repeat=W)):
            hash_count = 0
            for row in range(H):
                if h[row]:
                    continue
                else:
                    for col in range(W):
                        if C[row][col] == '#' and w[col] == 0:
                            hash_count += 1
            
            if hash_count == K:
                res += 1
    
    print(res)

if __name__ == '__main__':
    main()