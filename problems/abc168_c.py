import math

def main():
    a, b, h, m = map(int, input().split())

    hourAngle = math.pi * (h * 30 + m * 0.5) / 180
    minuteAngle = math.pi * (m * 6) / 180

    hourX = a * math.sin(hourAngle)
    hourY = a * math.cos(hourAngle)

    minuteX = b * math.sin(minuteAngle)
    minuteY = b * math.cos(minuteAngle)

    res = ((hourX - minuteX)**2 + (hourY - minuteY)**2)**0.5

    print(res)

if __name__ == '__main__':
    main()