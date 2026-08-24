class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        l, r = 0, x // 2 + 1

        while l + 1 < r:
            m = l + (r - l) // 2
            if m * m == x:
                return m

            elif m * m < x:
                l = m

            else:
                r = m

        return l