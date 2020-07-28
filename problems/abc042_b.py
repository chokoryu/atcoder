def main():
    n, l = map(int, input().split())
    S = list(input() for _ in range(n))

    print(''.join(sorted(S)))

if __name__ == '__main__':
    main()