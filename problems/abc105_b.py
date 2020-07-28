# ABC105 B

def main():
    n = int(input())
    res = 'No'

    for i in range(100 // 4):
        for j in range((100-i) // 7):
            if 4 * i + 7 * j == n:
                res = 'Yes'
                break
    
    print(res)

if __name__ == '__main__':
    main()