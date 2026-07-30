class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if (s[left].isalnum() and s[right].isalnum()) and s[left].lower() != s[right].lower():
                return False

            if s[left].isalnum() is False:
                left += 1

            elif s[right].isalnum() is False:
                right -= 1
                
            else:   
                left, right = left + 1, right - 1

        return True