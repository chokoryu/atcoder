# ABC165 D

def main():
    a, b, n = map(int, input().split())

    max = 0

    for i in range(n+1):
        res = ((a*i) // b) - a * (i // b)

        if res >= max:
            max = res
    
    print(max)

if __name__ == '__main__':
    main()