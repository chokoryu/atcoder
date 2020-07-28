# ABC053 B

def main():
    s = input()

    print(len(s[s.index('A'):len(s)-s[::-1].index('Z')]))

if __name__ == '__main__':
    main()