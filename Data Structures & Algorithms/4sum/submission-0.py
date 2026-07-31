class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        n = len(nums)
        nums.sort()

        for i in range(n):
            for j in range(i + 1, n):
                newTarget = target - nums[i] - nums[j]
                left, right = j + 1, n - 1

                while left < right:
                    if nums[left] + nums[right] == newTarget:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left, right = left + 1, right - 1

                    elif nums[left] + nums[right] < newTarget:
                        left += 1

                    else:
                        right -= 1


        return list(result)