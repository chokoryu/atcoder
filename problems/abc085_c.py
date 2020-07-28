# ABC085 C

def main():
    n, Y = map(int, input().split())

    total = 0
    flag = False
    res = [-1] * 3

    for x in range(n+1):
        total = 10000 * x

        if total == Y and x == n:
            res = [x, 0, 0]
            break

        for y in range(n-x+1):
            z = n - x - y
            total = 10000 * x + 5000 * y + 1000 * z

            if total == Y:
                res = [x, y, z]
                flag = True
                break
        
        if flag:
            break

    print(res[0], res[1], res[2])

if __name__ == '__main__':
    main()