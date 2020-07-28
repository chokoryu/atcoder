def main():
    a, b, c, x, y = map(int, input().split())

    minPrice = 10**20

    for i in range(2 * (x + y) + 1):
        pizzaC = i * c
        pizzaB = max(0, y - i // 2) * b
        pizzaA = max(0, x - i // 2) * a

        price = pizzaA + pizzaB + pizzaC
        
        if price < minPrice:
            minPrice = price

    print(minPrice)

if __name__ == '__main__':
    main()