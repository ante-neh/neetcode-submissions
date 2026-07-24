class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] > prices[i]:
                maxProfit += prices[i - 1] - min 
                min = prices[i]
        
        maxProfit += prices[-1] - min
        return maxProfit
