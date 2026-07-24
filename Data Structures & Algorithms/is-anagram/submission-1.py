class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = Counter(s), Counter(t)

        for c in t:
          if sCount[c] != tCount[c]:
            return False

        return True if len(s) == len(t) else False 