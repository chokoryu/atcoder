# hitachi2020 D

def main():
    n, t = map(int, input().split())
    cost = []
    for i in range(n):
        a, b = map(int, input().split())
        cost.append([a, b])

    start_time = 0
    shop_count = 0

    while True:
        min_time = 10**10

        for pair in cost:
            a, b = pair[0], pair[1]
            time = start_time + 1
            time = time + (a * time) + b
            
            if time < min_time:
                min_time = time
                pop_index = cost.index(pair)
            elif time == min_time:
                cost_time = time + 1 + (a * (time + 1) + b)
                cost_min_time = min_time + 1 + (cost[pop_index][0] * (min_time + 1) + cost[pop_index][1])

                if cost_time > cost_min_time:
                    min_time = time
                    pop_index = cost.index(pair)
        
        start_time = min_time
        cost.pop(pop_index)
        

        if min_time <= t + 0.5:
            shop_count += 1
            if len(cost) == 0:
                break
        else:
            break

    print(shop_count)

if __name__ == "__main__":
    main()