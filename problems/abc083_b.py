# ABC083 B

def main():
    n, a, b = map(int, input().split())

    sums = []

    for i in range(1, n+1):
        c = 0
        for num in str(i):
            c += int(num)
        
        if a <= c <= b:
            sums.append(i)
    
    print(sum(sums))

if __name__ == '__main__':
    main()