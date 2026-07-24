class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)
        
        return False

        # time complexity O(n) but the best case is relatively faster compared to the counter approach 
        # space complexity O(n) 