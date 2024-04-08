def max_profit(prices):
    
    if not prices or len(prices) < 2:
        return 0,0,0

    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(1, len(prices)):
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            buy_day = prices.index(min_price) + 1
            sell_day = i + 1

        min_price = min(min_price, prices[i])

    return max_profit, buy_day, sell_day

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4, 9, 2, 8]
    max_profit, buy_day, sell_day = max_profit(prices)
    print(f"Maximum Profit: {max_profit} (Buy on day {buy_day} (price = {prices[buy_day-1]}) and sell on day {sell_day} (price = {prices[sell_day-1]}))")
