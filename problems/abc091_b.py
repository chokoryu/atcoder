def main():
    n = int(input())
    S = {}

    for _ in range(n):
        s = input()

        if s in S:
            S[s] +=1
        else:
            S[s] = 1
    
    m = int(input())
    
    for _ in range(m):
        t = input()

        if t in S:
            S[t] -= 1
        else:
            S[t] = -1
    
    print(max(0, max(list(S.values()))))

if __name__ == '__main__':
    main()