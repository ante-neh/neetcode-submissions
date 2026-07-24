class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)


    def merge(self, nums1, nums2):
        nums = []
        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1

            else:
                nums.append(nums2[p2])
                p2 += 1

        if p1 < len(nums1):
            nums.extend(nums1[p1:])
        if p2 < len(nums2):
            nums.extend(nums2[p2:])

        return nums