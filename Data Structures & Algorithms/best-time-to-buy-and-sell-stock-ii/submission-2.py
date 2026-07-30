class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, cur = 0, prices[0]

        for price in prices:
            if price >= cur:
                maxProfit += price - cur
                cur = price
            else:
                cur = price

        return maxProfit


