from collections import deque

def main():
    n, m = map(int, input().split())
    rooms = list([] for _ in range(n))

    for _ in range(m):
        a, b = map(int, input().split())

        rooms[a-1].append(b-1)
        rooms[b-1].append(a-1)
    
    q = deque()
    q.append(0)

    dist = [False for _ in range(n)]
    dist[0] = 0

    while len(q):
        now = q.popleft()

        for nextRoom in rooms[now]:
            if dist[nextRoom] != False:
                continue
            else:
                dist[nextRoom] = now + 1
                q.append(nextRoom)
    
    if False not in dist:
        dist[0] = 'Yes'

        for i in range(len(dist)):
            if i == 0:
                print(dist[i])
            else:
                print(dist[i])
    else:
        print('No')

if __name__ == '__main__':
    main()