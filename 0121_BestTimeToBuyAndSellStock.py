class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxPrice, profit = prices[-1], 0
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > maxPrice:
                maxPrice = prices[i]
            else:
                profit = max(profit, maxPrice - prices[i])
        return profit