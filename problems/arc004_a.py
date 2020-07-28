# ARC004 A

def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]

    maxDist = 0

    for point1 in points:
        for point2 in points:
            dist = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
            if dist > maxDist:
                maxDist = dist
    
    print(maxDist)

if __name__ == '__main__':
    main()