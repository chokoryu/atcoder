import math

def main():
    n = int(input())

    divs = make_divisors(n)
    divs.pop(0)

    res = 0
    mult = 1
    A = []

    print(divs)

    if len(divs):
        for num in divs:
            if len(factorization(num)) == 1:
                mult = mult * num
                A.append(num)
                res += 1
                if mult == n:
                    break
    
    print(res, A)

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr 

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

if __name__ == '__main__':
    main()