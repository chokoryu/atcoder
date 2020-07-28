def main():
    w, h, n = map(int, input().split())

    corners = [0, 0, w, h]

    for i in range(n):
        x, y, a = map(int, input().split())

        if a == 1:
            if x > corners[0]:
                corners[0] = x
        elif a == 2:
            if x < corners[2]:
                corners[2] = x
        elif a == 3:
            if y > corners[1]:
                corners[1] = y
        else:
            if y < corners[3]:
                corners[3] = y
    
    width = corners[2] - corners[0]
    height = corners[3] - corners[1]

    if width < 0 or height < 0:
        print(0)
    else:
        print(width * height)

if __name__ == '__main__':
    main()