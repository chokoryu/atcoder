def main():
    k, s = map(int, input().split())

    res = 0

    for x in range(k+1):
        for y in range(k+1):
            z = s - (x + y)
            if z <= k and z >= 0:
                res += 1
        
    print(res)

if __name__ == '__main__':
    main()