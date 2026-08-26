class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles) + 1

        while l + 1 < r:
            m = l + (r - l) // 2
            if self.isPossible(m, h, piles):
                r = m

            else:
                l = m

        return r

    def isPossible(self, k, h, piles):
        currentTime = 0

        for pile in piles:
            currentTime += math.ceil(pile / k)
            if currentTime > h:
                return False

        return True if currentTime <= h else False
