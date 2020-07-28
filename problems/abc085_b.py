# ABC085 A

def main():
    n = int(input())
    D = []
    for i in range(n):
        d = int(input())
        D.append(d)
    
    print(len(set(D)))

if __name__ == '__main__':
    main()