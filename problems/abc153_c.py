# ABC153 C

n, k = map(int, input().split())
H = list(map(int, input().split()))

H.sort()

for _ in range(k):
    if len(H) != 0:
        H.pop()
    else:
        break

print(sum(H))