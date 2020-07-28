# ABC166 C

def main():
    n, m = map(int, input().split())
    H = list(map(int, input().split()))
    
    towers = []
    for _ in range(n):
        towers.append([])
    
    good_tower_count = 0

    for _ in range(m):
        a, b = map(int, input().split())
        #print(a, b)
        towers[a-1].append(b-1)
        towers[b-1].append(a-1)
        #print(towers)
    
    # for each of the towers
    for i in range(n):
        good_flags = []

        # check if the tower is taller than the neighbour towers
        for j in range(len(towers[i])):
            if H[i] > H[towers[i][j]]:
                good_flags.append(True)
            else:
                good_flags.append(False)
        
        if (False not in good_flags) or len(towers[i]) == 0:
            good_tower_count += 1
            #print(i)
    
    print(good_tower_count)
    


if __name__ == '__main__':
    main()