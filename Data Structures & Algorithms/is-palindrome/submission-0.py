class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum() and s[left].lower() != s[right].lower():
                return False
            elif not s[left].isalnum() or not s[right].isalnum():
                if not s[left].isalnum():
                    left += 1
                
                if not s[right].isalnum():
                    right -= 1
            else:
                left, right = left + 1, right - 1


        return True 

