def main():
    n, k = map(int, input().split())

    print(min(n % k, 1))

if __name__ == '__main__':
    main()