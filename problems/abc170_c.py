def main():
    x, n = map(int, input().split())
    if n != 0:
        P = list(map(int, input().split()))

        maxP = max(P)

        numList = [0 for i in range(maxP+2)]

        for num in P:
            numList[num] += 1
        
        maxRes = 101
        maxCount = 0
        minRes = 101
        minCount = 0

        for i in range(x, maxP+2):
            maxCount += 1
            if numList[i] == 0:
                maxRes = i
                break
        
        for i in range(x, -1, -1):
            minCount += 1
            if numList[i] == 0:
                minRes = i
                break

        if maxCount < minCount:
            print(maxRes)
        else:
            print(minRes)

    else:
        print(x)

    

if __name__ == '__main__':
    main()