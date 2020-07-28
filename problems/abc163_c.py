# ABC163 C

def main():
    n = int(input())
    A = list(map(int, input().split()))

    res = [0] * n

    for i in A:
        res[i-1] += 1
    
    for num in res:
        print(num)

if __name__ == '__main__':
    main()