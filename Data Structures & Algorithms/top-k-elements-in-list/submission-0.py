class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounter = Counter(nums)
        numsCounterSorted = sorted(numsCounter.items(), key=lambda x: x[1], reverse=True)

        result = [] 

        for value in numsCounterSorted:
            result.append(value[0])
            k -= 1
            if k == 0:
                break 

        return result