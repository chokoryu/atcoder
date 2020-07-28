# ABC159 C

def main():
    l = int(input())

    if l % 3:
        a = l / 3
        print(a * a * (l - 2*a))
    else:
        print((l / 3)**3)

if __name__ == '__main__':
    main()