def main():
    N = int(input())
    A = list(map(int, input().split()))

    res = []
    xorSum = 0

    for i in range(0,N-1):
        xorSum ^= A[i]
    
    res.append(xorSum)
    A_reversed = A[::-1]

    for i in range(N-1):
        xorSum = xorSum ^ A_reversed[i] ^ A_reversed[i+1]
        res.append(xorSum)
    
    print(" ".join(map(str, res[::-1])))

if __name__ == '__main__':
    main()