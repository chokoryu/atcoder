# ABC154 D

n, k = map(int, input().split())
P = list(map(int, input().split()))

sumP = []

for i in range(1, n-k+2):
    sumP.append(sum(P[i:i+k]))

print((max(sumP) + k) / 2)