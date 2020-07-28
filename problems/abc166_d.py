# ABC166 D

def main():
    x = int(input())
    res = 0

    for i in range(-64, 65):
        for j in range(-64, 65):
            if i**5 - j**5 == x:
                res = [i, j]
                break
        if res:
            break
    
    print(res[0], res[1])
                

if __name__ == '__main__':
    main()