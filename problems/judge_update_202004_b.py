# judge_update_202004 B

def main():
    n = int(input())

    R = []
    B = []

    for i in range(n):
        x, c = input().split()
        x = int(x)
        
        if c == 'R':
            R.append(x)
        else:
            B.append(x)
    
    R.sort()
    B.sort()

    for ball in R:
        print(ball)
    
    for ball in B:
        print(ball)

if __name__ == '__main__':
    main()