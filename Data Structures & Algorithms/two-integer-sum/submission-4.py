class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        numToIndex = {}

        for index, num in enumerate(nums):
            if target - num in numToIndex:
                return [numToIndex[target - num], index]

            numToIndex[num] = index

        # time complexity O(n)
        # space complexity O(n)