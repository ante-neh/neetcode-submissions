class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, minLength = 0, 10 ** 5 + 1
        curSum = 0

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minLength = min(minLength, r - l + 1)
                curSum -= nums[l]
                l += 1

        return minLength if minLength != 10 ** 5 + 1 else 0