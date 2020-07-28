def main():
    a = input()

    upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if a in upper:
        print('A')
    else:
        print('a')

if __name__ == '__main__':
    main()