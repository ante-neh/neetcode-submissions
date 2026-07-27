class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0]) 
        self.prefixSum = [[0] * (cols + 1) for r in range(rows + 1)]
        for r in range(rows):
            prefixSum = 0
            for c in range(cols):
                prefixSum += matrix[r][c] 
                self.prefixSum[r + 1][c + 1] = prefixSum + self.prefixSum[r][c + 1]




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1+ 1, row2 + 1, col1 + 1, col2 + 1
        return self.prefixSum[r2][c2] - self.prefixSum[r2][c1 - 1] - self.prefixSum[r1 - 1][c2] + self.prefixSum[r1 - 1][c1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)