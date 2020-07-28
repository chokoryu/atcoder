# Panasonic2020 B

h, w = map(int, input().split())

if h == 1 or w == 1:
    print(1)
elif (h * w) % 2:
    print(1 + (h * w) // 2)
else:
    print(h * w // 2)