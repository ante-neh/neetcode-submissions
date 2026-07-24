class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumToDiffPair = defaultdict(int)

        for index, num in enumerate(nums):
          if target - num in sumToDiffPair:
            return [sumToDiffPair[target - num], index]

          sumToDiffPair[num] = index
          
