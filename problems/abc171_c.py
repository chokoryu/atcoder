def main():
    N = int(input())

    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    name = []

    while True:
        if N % 26:
            res = N % 26
        else:
            res = 26

        name.append(alphabet[res-1])

        if N - res == 0:
            break
        else:
            N = (N - res) // 26
    
    print(''.join(name[::-1]))

if __name__ == '__main__':
    main()