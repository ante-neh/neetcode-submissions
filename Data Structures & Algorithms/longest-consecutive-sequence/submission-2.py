class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestConsecutive = 0

        for num in numsSet:
            currentNum = num
            currentMax = 1

            if num - 1 not in numsSet:
                while currentNum + 1 in numsSet:
                    currentNum += 1
                    currentMax += 1

                longestConsecutive = max(longestConsecutive, currentMax)

        return longestConsecutive
            