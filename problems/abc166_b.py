# ABC166 B

def main():
    n, k = map(int, input().split())
    
    sunuke = [0] * n

    for i in range(k):
        d = int(input())
        A = list(map(int, input().split()))

        for j in A:
            sunuke[j-1] += 1
    
    print(sunuke.count(0))



if __name__ == '__main__':
    main()