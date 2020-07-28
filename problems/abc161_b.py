# ABC161 B

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    sortedA = sorted(A)[::-1]

    if sortedA[m-1] >= sum(A) / (4*m):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()