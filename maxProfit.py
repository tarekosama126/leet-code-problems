def maxProfit(prices) -> int:
    maxprofit = 0
    i = 0
    j = 1
    size = len(prices) - 1
    while j <= size:
        if prices[i] < prices[j]:
            maxprofit += (prices[j] - prices[i])
        i += 1
        j += 1
    return maxprofit