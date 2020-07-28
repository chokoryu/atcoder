def main():
    a, b = input().split()

    a = int(a)
    b = int(round(float(b) * 100, 0))

    res = a * b

    print(int(res // 100))

if __name__ == '__main__':
    main()