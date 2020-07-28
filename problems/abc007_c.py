from collections import deque

def main():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1

    C = list(list(input()) for _ in range(r))

    queue = deque()
    queue.append((sy, sx))

    notSeen = -1
    dist = list([notSeen for _ in range(c)] for __ in range(r))
    dist[sy][sx] = 0

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)

    while len(queue):
        now = queue.popleft()
        y, x = now

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if dist[ny][nx] != notSeen:
                continue
            if C[ny][nx] == '#':
                continue

            dist[ny][nx] = dist[y][x] + 1
            queue.append((ny, nx))
    
    print(dist[gy][gx])

if __name__ == '__main__':
    main()