def main():
    n = int(input())

    minRes = 10 ** 10

    for a in range(1, 10** 5 + 1):
        if n % a == 0:
            b = int(n / a)

            res = max(len(str(a)), len(str(b)))

            if res < minRes:
                minRes = res
    
    print(minRes)

if __name__ == '__main__':
    main()