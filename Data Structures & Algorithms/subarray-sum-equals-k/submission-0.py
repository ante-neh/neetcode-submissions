class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumCount = collections.defaultdict(int)
        curSum = 0
        count = 0
        sumCount[0] = 1
        for num in nums:
            curSum += num
            count += sumCount[curSum - k]
            sumCount[curSum] += 1

        return count
         