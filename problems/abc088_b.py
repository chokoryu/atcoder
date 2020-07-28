# ABC088 B

def main():
    n = int(input())
    A = list(map(int, input().split()))

    Alice = 0
    Bob = 0
    A_sorted = sorted(A)[::-1]

    for i in range(n):
        if i % 2:
            Bob += A_sorted[i]
        else:
            Alice += A_sorted[i]
    
    print(Alice - Bob)

if __name__ == '__main__':
    main()