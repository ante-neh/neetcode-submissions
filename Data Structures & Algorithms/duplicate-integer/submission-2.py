class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCount = Counter(nums)
        for _, count in numsCount.items():
            if count > 1:
                return True 


        return False  

#TC => O(n)
#SC => O(n)