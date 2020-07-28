def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    A_sorted = sorted(A)

    res = 0

    for kids in A_sorted:
        x = x - kids
        
        if x >= 0:
            res += 1
    
    if x > 0:
        print(res - 1)
    else:
        print(res)

if __name__ == '__main__':
    main()