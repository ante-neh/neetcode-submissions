class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCount = Counter(nums)
        for val, count in numsCount.items():
            if count > 1:
                return True

        return False