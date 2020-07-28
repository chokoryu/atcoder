def main():
    s = input()

    bucket = list('' for _ in range(26))

    for char in s:
        bucket[ord(char) - 97] = char
    
    try:
        print(chr(bucket.index('') + 97))
    except:
        print('None')

if __name__ == '__main__':
    main()