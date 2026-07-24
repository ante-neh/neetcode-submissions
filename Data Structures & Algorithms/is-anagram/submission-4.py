class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = Counter(s), Counter(t)

        return sCount == tCount 


# TC O(n)
# SC O(n)