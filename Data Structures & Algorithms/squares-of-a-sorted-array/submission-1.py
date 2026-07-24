class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        resIndex = len(nums) - 1
        result = [0] * len(nums)

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[resIndex] = nums[left] * nums[left]
                left += 1
            else:
                result[resIndex] = nums[right] * nums[right]
                right -= 1
            resIndex -= 1

        return result