class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(l, r - 1, s) or self.isPalindrome(l + 1, r, s)
            l, r = l + 1, r - 1

        return True 

    def isPalindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True 