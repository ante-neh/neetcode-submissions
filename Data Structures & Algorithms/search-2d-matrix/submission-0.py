class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = -1, row * col

        while l + 1 < r:
            m = l + (r - l) // 2
            val = matrix[m // col][m % col]

            if val == target:
                return True
            elif val > target:
                r = m 
            else:
                l = m
            
        return False