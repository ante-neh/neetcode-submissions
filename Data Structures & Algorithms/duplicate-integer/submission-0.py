class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCount = defaultdict(int) 

        for num in nums:
          numsCount[num] += 1
        
        for item in numsCount.items():
          if item[1] > 1:
            return True

        return False

        