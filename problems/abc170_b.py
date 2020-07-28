def main():
    x, y = map(int, input().split())

    res = 'No'

    for i in range(x+1):
        crane = i
        turtle = x - i

        if crane*2 + turtle*4 == y:
            res = 'Yes'
            break
    
    print(res)

if __name__ == '__main__':
    main()