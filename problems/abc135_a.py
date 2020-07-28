# abc 135 A

a, b = map(int, input().split())

res = a + b

if res % 2:
    print("IMPOSSIBLE")
else:
    print(res // 2)