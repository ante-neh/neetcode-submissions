class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        cur, left, right = 0, 0, len(nums) - 1

        while cur <= right:
            if nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1

            elif nums[cur] == 1:
                cur += 1

            else:
                nums[cur], nums[left] = nums[left], nums[cur]
                cur, left = cur + 1, left + 1


            