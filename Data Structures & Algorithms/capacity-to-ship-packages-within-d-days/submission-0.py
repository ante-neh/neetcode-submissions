class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        totalWeight = sum(weights)
        l, r = 0, totalWeight + 1

        while l + 1 < r:
            m = l + (r - l) // 2

            if self.isPossible(weights, m, days):
                r = m

            else:
                l = m

        return r
        
    def isPossible(self, weights, k, days):
        currentWeight, currentDays = 0, 1

        for weight in weights:
            if weight > k:
                return False

            if currentWeight + weight > k:
                currentDays += 1
                currentWeight = 0

            currentWeight += weight

        return currentDays <= days