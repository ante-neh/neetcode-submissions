class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = defaultdict(int)
        tCount = defaultdict(int)

        for c in s:
            sCount[c] += 1

        for c in t:
            tCount[c] += 1

        if len(sCount) != len(tCount):
            return False
            
        for c in s:
            if sCount[c] != tCount[c]:
                return False


        return True

        # time complexity O(n)
        # space complexity O(n)