# ABC086 C

def main():
    n = int(input())
    
    res = 'Yes'

    for i in range(n):
        t, x, y = map(int, input().split())
        
        if i != 0:
            t, x, y = t - t_prev, x - x_prev, y - y_prev

        if abs(x) + abs(y) > t:
            res = 'No'
            break
        elif (not t%2 and (x+y)%2) or (t%2 and not ((x+y)%2)):
            res = 'No'
            break
        
        t_prev, x_prev, y_prev = t, x, y
    
    print(res)

if __name__ == '__main__':
    main()