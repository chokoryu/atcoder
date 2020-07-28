# ABC167 C

def main():
    n, m, x = map(int, input().split())
    List = []
    
    for _ in range(n):
        tmp = list(map(int, input().split()))
        List.append(tmp)

    minCost = 10**20

    for i in range(1, 2**n):
        inBit = ''.join(['{:0', str(n), 'b}']).format(i)[::-1]
        knowledge = [0 for _ in range(m)]
        cost = 0

        for bit in range(len(inBit)):
            if inBit[bit] == '1':
                cost += List[bit][0]
                for j in range(m):
                    knowledge[j] += List[bit][j+1]
        
        requirement = [a >= b for (a, b) in zip(knowledge, [x for _ in range(m)])]
        
        if False not in requirement and cost < minCost:
            minCost = cost
    
    if minCost == 10**20:
        print(-1)
    else:
        print(minCost)

if __name__ == '__main__':
    main()