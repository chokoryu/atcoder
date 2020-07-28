# ABC124 A

def main():
    AB = list(map(int, input().split()))

    result = 0

    for i in range(2):
        max_num = max(AB)
        result += max_num
        AB[AB.index(max_num)] = max_num - 1
    
    print(result)

if __name__ == '__main__':
    main()