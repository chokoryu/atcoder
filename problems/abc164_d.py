# ABC164 D

def main():
    s = input()
    count = 0
    #results = []

    for i in range(len(s)-4):
        for j in range(i+5, len(s)+1):
            if int(s[i:j]) % 2019 == 0:
                count += 1
                #results.append((i+1,j))
    
    print(count)
    #print(len(s))
    #print(results)

if __name__ == '__main__':
    main()