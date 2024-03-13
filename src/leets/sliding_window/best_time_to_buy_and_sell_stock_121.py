def best_time_to_buy_and_sell_stock_121(stocks):
    max_profit = 0
    n = len(stocks)
    l, r = 0, 1
    while l < r and r < n:
        if stocks[l] < stocks[r]:
            max_profit = max(max_profit, stocks[r] - stocks[l])
            r += 1
        else:
            l = r
            r += 1
    return max_profit
