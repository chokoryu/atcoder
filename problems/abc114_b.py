def main():
    s = input()

    minRes = 10000

    for num in range(len(s)-2):
        res = abs(int(s[num:num+3]) - 753)

        if res < minRes:
            minRes = res
    
    print(minRes)

if __name__ == '__main__':
    main()