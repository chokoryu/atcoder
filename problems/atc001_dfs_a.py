from collections import deque

def main():
    h, w = map(int, input().split())

    grid = []
    
    for i in range(h):
        row = list(input())

        if 's' in row:
            sh = i
            sw = row.index('s')
        if 'g' in row:
            gh = i
            gw = row.index('g')
        
        grid.append(row)

    stack = deque()
    stack.append((sh, sw))

    notSeen = 1<<60
    gridList = [[notSeen for _ in range(w)] for __ in range(h)]
    gridList[sh][sw] = 0

    dh = (0, 1, 0, -1)
    dw = (1, 0, -1, 0)

    goalFlag = 'No'

    while len(stack):
        ch, cw = stack.pop()

        for di in range(4):
            nh = ch + dh[di]
            nw = cw + dw[di]

            if nh < 0 or nh >= h or nw < 0 or nw >= w:
                continue
            if grid[nh][nw] == 'g':
                goalFlag = 'Yes'
            if gridList[nh][nw] != notSeen:
                continue
            if grid[nh][nw] == '#':
                continue

            gridList[nh][nw] = gridList[ch][cw] + 1
            stack.append((nh, nw))
    
    print(goalFlag)

if __name__ == '__main__':
    main()