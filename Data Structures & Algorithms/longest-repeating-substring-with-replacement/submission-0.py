class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        maxFreq = l = 0
        longest = 0

        for r in range(len(s)):
            charCount[s[r]] += 1
            maxFreq = max(maxFreq, charCount[s[r]])

            while (r - l + 1) - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest