class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        results = []

        for num in nums:
            results.append(product)
            product *= num

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= product
            product *= nums[i]

        return results