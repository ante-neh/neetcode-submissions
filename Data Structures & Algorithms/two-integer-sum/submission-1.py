class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffToIndex = defaultdict(int)

        for index, num in enumerate(nums):
            if num in diffToIndex:
                return [diffToIndex[num], index]

            diffToIndex[target - num] = index