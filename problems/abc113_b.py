# ABC113 B

def main():
    n = int(input())
    t, a = map(int, input().split())
    H = list(map(int, input().split()))

    differences = []

    for height in H:
        temp = t - height * 0.006
        differences.append(abs(temp - a))
    
    print(differences.index(min(differences)) + 1)

if __name__ == '__main__':
    main()