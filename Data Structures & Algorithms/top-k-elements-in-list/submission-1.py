class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = Counter(nums)
        numsCount = sorted(numsCount.items(), key=lambda x: x[1], reverse=True)

        result = []

        for key, value in enumerate(numsCount):
            if k == 0:
                break

            result.append(value[0])
            k -= 1

        return result

    # time complexity O(nlogn)
    # space complexity O(n)
