# ABC162 C

import math

def main():
    k = int(input())

    res = []

    for i in range(1, k+1):
        for j in range(1, k+1):
            for l in range(1, k+1):
                gcd = math.gcd(i, j)
                if gcd==1:
                    res.append(1)
                else:
                    res.append(math.gcd(gcd ,l))
    
    print(sum(res))

def gcd3(a, b, c):
    ans = math.gcd(math.gcd(a, b), c)
    
    return ans

if __name__ == '__main__':
    main()