# ABC135 B

def main():
    n = int(input())
    P = list(map(int, input().split()))

    wrong_order = 0

    for i in range(n):
        if P[i] != i + 1:
            wrong_order += 1

    if wrong_order <= 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()