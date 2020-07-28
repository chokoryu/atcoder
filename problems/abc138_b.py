# abc138 b

def main():
    n = int(input())
    A = list(map(int, input().split()))
    reciprocal = 0

    for i in range(n):
        reciprocal += 1/A[i]
    
    print(1/reciprocal)

if __name__ == '__main__':
    main()