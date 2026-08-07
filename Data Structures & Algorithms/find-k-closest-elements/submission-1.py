class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0

        for r in range(len(arr)):
            while r - l + 1 > k and abs(arr[r] - x) < abs(arr[l] - x):
                l += 1

        return arr[l: l + k]

