# ABC049 C

def main():
    s = input()

    if s.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', ''):
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()