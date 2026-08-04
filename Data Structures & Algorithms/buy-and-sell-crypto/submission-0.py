class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0

        for r, price in enumerate(prices):
            if price >= prices[l]:
                maxProfit = max(maxProfit, price - prices[l])

            else:
                l = r

        return maxProfit