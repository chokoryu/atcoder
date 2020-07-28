# ABC159 B

def main():
    s = input()
    
    n = len(s)
    m = (n-1)//2
    o = (n+3)//2
    p = s[:m]
    q = s[o-1:]

    if s == s[::-1]:
        if p == p[::-1]:
            if q == q[::-1]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()