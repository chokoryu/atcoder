# ABC129 A

def main():
    p, q, r = map(int, input().split())
    
    resList = [p+q, p+r, q+r]

    print(min(resList))

if __name__ == '__main__':
    main()