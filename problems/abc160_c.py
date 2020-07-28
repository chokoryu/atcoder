# ABC160 C

def main():
    k, n = map(int, input().split())
    A = list(map(int, input().split()))
    
    maxIndex = 0
    maxDist = 0
    
    for i in range(n):
        if i == n - 1:
            gap = A[0]+k - A[i]
        else:
            gap = A[i+1] - A[i]
        
        if gap >= maxDist:
            maxDist = gap
            maxIndex = i
    
    if maxIndex == n - 1:
        print(A[-1] - A[0])
    else:
        print((A[maxIndex]+k) - A[maxIndex+1])            

if __name__ == '__main__':
    main()