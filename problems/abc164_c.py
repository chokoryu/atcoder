# ABC164 C

def main():
    n = int(input())
    S = []

    for _ in range(n):
        s = input()
        S.append(s)
    
    print(len(set(S)))

if __name__ == '__main__':
    main()