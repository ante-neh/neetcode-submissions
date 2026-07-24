class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)

        return sCount == tCount

        # time complexity O(n)
        # space complexity O(n)