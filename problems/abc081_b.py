# ABC081 B

def main():
    n = int(input())
    A = list(map(int, input().split()))

    result = 0
    flag = 0
    
    while True:
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            else:
                flag = 1
                break
        
        if flag == 1:
            break

        result += 1
    
    print(result)

if __name__ == '__main__':
    main()