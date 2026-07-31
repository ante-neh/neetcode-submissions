class Solution:

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.check(s, left + 1, right) or self.check(s, left, right - 1)

            left, right = left + 1, right - 1

        return True 

    def check(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left, right = left + 1, right - 1

        return True 