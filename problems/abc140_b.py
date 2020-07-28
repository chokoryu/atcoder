# ABC140 B

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0

    for i in range(n):
        satisfaction += B[A[i] - 1]
        if 0 < i < n and A[i] == A[i-1] + 1:
            satisfaction += C[A[i]-2]
    
    print(satisfaction)

if __name__ == '__main__':
    main()