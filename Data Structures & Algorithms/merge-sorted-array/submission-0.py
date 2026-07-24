class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mr, nr = m - 1, n -1
        cur = n + m - 1

        while cur >= 0 and mr >= 0 and nr >= 0:
            if nums1[mr] >= nums2[nr]:
                nums1[cur], nums1[mr] = nums1[mr], nums1[cur]
                mr -= 1
            else:
                nums1[cur], nums2[nr] = nums2[nr], nums1[cur]
                nr -= 1

            cur -= 1

        while nr >= 0:
            nums1[cur], nums2[nr] = nums2[nr], nums1[cur]
            nr -= 1
            cur -= 1

        while mr >= 0:
            nums1[cur], nums1[mr] = nums1[mr], nums1[cur]
            mr -= 1
            cur -= 1
