# ABC068 B

def main():
    n = int(input())

    print(2**(len(bin(n)[2:])-1))

if __name__ == '__main__':
    main()