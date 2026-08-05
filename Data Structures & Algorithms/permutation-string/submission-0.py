class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        k = len(s1)

        for r in range(len(s2)):
            while r - l + 1 > k:
                l += 1

            if r - l + 1 == k and self.check(s1, s2[l: r + 1]):
                return True

        return False
        
    def check(self, s1, s2):
        return Counter(s1) == Counter(s2)