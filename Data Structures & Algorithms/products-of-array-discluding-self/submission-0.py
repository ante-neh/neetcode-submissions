class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        result = []

        for num in nums:
            result.append(total)
            total *= num 

        total = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= total
            total *= nums[i]

        return result
        