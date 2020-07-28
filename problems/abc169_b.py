def main():
    n = int(input())
    A = list(map(int, input().split()))

    res = 1

    if 0 in A:
        res = 0
    else:
        for num in A:
            res = res * num
            if res > 10**18:
                res = -1
                break
    print(res)

if __name__ == '__main__':
    main()