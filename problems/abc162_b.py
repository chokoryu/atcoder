# ABC162 B

def main():
    n = int(input())

    res = []

    for i in range(1, n+1):
        if i%3==0 or i%5==0:
            continue
        else:
            res.append(i)
    
    print(sum(res))


if __name__ == '__main__':
    main()