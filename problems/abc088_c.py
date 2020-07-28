def main():
    C = [list(map(int, input().split())) for _ in range(3)]

    res = 'No'

    for i in range(101):
        b1 = C[0][0] - i
        b2 = C[0][1] - i
        b3 = C[0][2] - i
        a2 = C[1][0] - b1
        a3 = C[2][0] - b1

        if C[1][1] == a2 + b2 and C[1][2] == a2 + b3 and C[2][1] == a3 + b2 and C[2][2] == a3 + b3:
            res = 'Yes'
            break
    
    print(res)

if __name__ == '__main__':
    main()