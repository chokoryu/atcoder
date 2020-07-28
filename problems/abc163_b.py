# ABC163 B

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    if sum(A) > n:
        print(-1)
    else:
        print(n - sum(A))

if __name__ == '__main__':
    main()