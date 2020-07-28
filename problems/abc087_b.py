# ABC087 B

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    result = 0

    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                total = 500 * i + 100 * j + 50 * k
                if total == x:
                    result += 1
    
    print(result)

if __name__ == '__main__':
    main()