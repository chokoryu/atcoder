# ABC160 B

def main():
    x = int(input())

    fivehundred = x // 500
    five = (x - (fivehundred * 500)) // 5

    print((fivehundred * 1000) + (five * 5))

if __name__ == '__main__':
    main()