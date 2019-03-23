import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minimum = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                profit = prices[i] - minimum
                if profit > max_profit:
                    max_profit = profit

        return max_profit
