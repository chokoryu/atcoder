# ABC165 C

import itertools

def main():
    n, m, q = map(int, input().split())
    List = []
    for i in range(q):
        a, b, c, d = map(int, input().split())
        List.append([a, b, c, d])
    
    max_total = 0

    for A in list(itertools.combinations_with_replacement(range(1, m+1),n)):
        total = 0
        for abcd in List:
            if A[abcd[1]-1] - A[abcd[0]-1] == abcd[2]:
                total += abcd[3]
        #print(total)
        if total >= max_total:
            max_total = total
    
    print(max_total)

if __name__ == '__main__':
    main()