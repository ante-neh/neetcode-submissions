class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffToIndexPair = defaultdict(int)
        for index, num in enumerate(nums):
            if num in diffToIndexPair:
                return [diffToIndexPair[num], index]

            diffToIndexPair[target - num] = index 