class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        for i in range(n):
            left, right = i + 1, n - 1
            target = 0 - nums[i]
            while left < right:
                if nums[left] + nums[right] == target:
                    result.add((nums[i], nums[left], nums[right]))
                    left, right = left + 1, right - 1
                    
                elif nums[left] + nums[right] < target:
                    left += 1

                else:
                    right -= 1

        return list(result)