# ABC167 B

def main():
    a, b, c, k = map(int, input().split())
    total = 0

    if a >= k:
        print(k)
    elif a+b >= k:
        print(a)
    else:
        print(a - (k - a - b))

if __name__ == '__main__':
    main()