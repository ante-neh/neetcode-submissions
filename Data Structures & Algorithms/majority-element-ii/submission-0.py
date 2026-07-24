
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numsCount = Counter(nums)
        majority = []
        for key, count in numsCount.items():
            if count > len(nums) // 3:
                majority.append(key)

        return majority