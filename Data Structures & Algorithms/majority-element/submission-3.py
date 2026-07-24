class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        numsCount = Counter(nums)

        for key, value in numsCount.items():
            if value >= math.ceil(n / 2):
                return key