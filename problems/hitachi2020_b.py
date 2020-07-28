# hitachi2020 B

def main():
    a, b, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min_price = min(A) + min(B)

    for i in range(m):
        x, y, c = map(int, input().split())
        
        if A[x-1] + B[y-1] - c < min_price:
            min_price = A[x-1] + B[y-1] - c

    print(min_price)

if __name__ == "__main__":
    main()