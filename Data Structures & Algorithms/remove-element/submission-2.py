class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            if nums[right] == val:
                right -= 1

            elif nums[left] != val:
                left += 1

            else:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        return left

    # time complexity O(n)
    # space complexity O(1)
    