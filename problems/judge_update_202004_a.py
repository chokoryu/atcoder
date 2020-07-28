# judge-update-202004 A

def main():
    s, l, r = map(int, input().split())

    if s <= l:
        print(l)
    elif s >= r:
        print(r)
    else:
        print(s)


if __name__ == '__main__':
    main()