import math
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
    elif (r1 + c1 == r2 + c2) or (r1 - c1 == r2 - c2) or (abs(r1 - r2) + abs(c1 - c2) <= 3):
        print(1)
    elif r2 - r1 > 0:
        if c2 - c1 > 0:
            # 2, x軸もy軸もプラス
            d = r2 - r1 + c1
            if abs(c2 - d) > 3:
                if (abs(r1 - r2) + abs(c1 - c2)) % 2:
                    print(3)
                else:
                    print(2)
            else:
                print(2)
        elif c2 - c1 < 0:
            # 1, x軸はプラス、y軸はマイナス
            d = r1 + c1 - r2
            if abs(d - c2) > 3:
                if (abs(r1 - r2) + abs(c1 - c2)) % 2:
                    print(3)
                else:
                    print(2)
            else:
                print(2)
        else: # x軸に沿ってプラスに移動
            if (abs(r1 - r2) + abs(c1 - c2)) % 2:
                print(3)
            else:
                print(2)
    elif r2 - r1 < 0:
        if c2 - c1 > 0:
            # 1, x軸はマイナス、y軸はプラス
            d = r1 + c1 - r2
            if abs(c2 - d) > 3:
                if (abs(r1 - r2) + abs(c1 - c2)) % 2:
                    print(3)
                else:
                    print(2)
            else:
                print(2)
        elif c2 - c1 < 0:
            # 2, x軸もy軸もマイナス
            d = r2 - r1 + c1
            if abs(c2 - d) >3:
                if (abs(r1 - r2) + abs(c1 - c2)) % 2:
                    print(3)
                else:
                    print(2)
            else:
                print(2)
        else: # x軸に沿ってマイナスに移動
            if (abs(r1 - r2) + abs(c1 - c2)) % 2:
                print(3)
            else:
                print(2)
    else: # x軸は移動無し
        if (abs(r1 - r2) + abs(c1 - c2)) % 2:
            print(3)
        else:
            print(2)

if __name__ == '__main__':
    main()