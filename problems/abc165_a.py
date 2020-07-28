# ABC165 A

def main():
    k = int(input())
    a, b = map(int, input().split())

    res = False

    for i in range(a, b+1):
        if i % k == 0:
            print('OK')
            res = True
            break
    
    if res == False:
        print('NG')

if __name__ == '__main__':
    main()