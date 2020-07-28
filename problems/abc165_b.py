# ABC165 B

def main():
    x = int(input())
    balance = 100
    year = 0

    while True:
        balance = int(balance * 1.01)
        year += 1
        if balance >= x:
            break
    
    print(year)

if __name__ == '__main__':
    main()