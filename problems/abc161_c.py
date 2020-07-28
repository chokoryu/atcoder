# ABC161 C

def main():
    n, k = map(int, input().split())

    minValue = 10e18

    if k == 1:
        print(0)
    elif k == 2:
        if n % 2:
            print(1)
        else:
            print(0)
    else:
        x = n
        while True:
            x = abs(x - k)

            if x < minValue:
                minValue = x
            elif x == minValue:
                print(x)
                break


if __name__ == '__main__':
    main()