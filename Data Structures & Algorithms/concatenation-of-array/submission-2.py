class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (n * 2)

        for i in range(n * 2):
            result[i] = nums[i % n ]

        return result

    # time complexity O(n)
    # space complexity O(n)