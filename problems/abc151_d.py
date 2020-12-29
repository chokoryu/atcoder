from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    H, W = map(int, input().split())

    grid = list(input() for _ in range(H))

    def bfs(H, W, SH, SW):
        q = deque()
        q.append((SH, SW))

        INF = -1
        dist = [[INF for _ in range(W)] for __ in range(H)]
        dist[SH][SW] = 0

        dh = (0, 1, 0, -1)
        dw = (1, 0, -1, 0)

        ret = 0

        while(len(q)):
            now = q.popleft()
            h, w = now

            for di in range(4):
                nh = h + dh[di]
                nw = w + dw[di]

                if nh < 0 or nh >= H or nw < 0 or nw >= W:
                    continue
                if grid[nh][nw] == '#':
                    continue
                if dist[nh][nw] != INF:
                    continue

                dist[nh][nw] = dist[h][w] + 1
                q.append((nh, nw))
                ret = max(ret, dist[nh][nw])

        return ret

    max_res = 0

    for SH in range(H):
        for SW in range(W):
            if grid[SH][SW] == '#':
                continue
            max_res = max(max_res, bfs(H, W, SH, SW))

    print(max_res)

if __name__ == '__main__':
    main()