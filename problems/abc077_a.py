def main():
    C1 = input()
    C2 = input()

    if C1[::-1] == C2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()