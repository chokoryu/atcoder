def main():
    n = int(input())

    if str(n)[-1] == '3':
        res = 'bon'
    elif str(n)[-1] in ['0', '1', '6', '8']:
        res = 'pon'
    else:
        res = 'hon'
    
    print(res)

if __name__ == '__main__':
    main()