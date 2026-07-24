class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        return sorted(s) == sorted(t)

        #brute force approach
        # time complexity O(nlogn)
        # space complexity O(n)