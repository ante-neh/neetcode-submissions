class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        sumDiffMap = defaultdict(int)
        sumDiffMap[0] = 1
        result = 0

        for num in nums:
            curSum += num
            diff = curSum - k

            if diff in sumDiffMap:
                result += sumDiffMap[diff]

            sumDiffMap[curSum] += 1

        return result 