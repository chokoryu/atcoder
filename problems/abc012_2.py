from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N = int(input())

    second = int(N % 60)
    minute = int(((N - second) / 60) % 60)
    hour = int(((N - second) / 60) // 60)

    ans_list = [second, minute, hour]

    for i in range(len(ans_list)):
        if len(str(ans_list[i])) == 1:
            ans_list[i] = '0' + str(ans_list[i])

    print("{}:{}:{}".format(ans_list[2], ans_list[1], ans_list[0]))

if __name__ == '__main__':
    main()