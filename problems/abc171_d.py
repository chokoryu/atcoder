def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    opeList = [list(map(int, input().split())) for _ in range(Q)]
    
    bucket = Counter(A)[0] * (10**5 + 1)
    sumA = sum(A)

    for num in A:
        bucket[num] += 1
    
    for ope in opeList:
        tmp = bucket[ope[0]]
        bucket[ope[0]] = 0
        bucket[ope[1]] += tmp
        sumA = sumA - ope[0] * tmp + ope[1] * tmp
        print(sumA)

if __name__ == '__main__':
    main()