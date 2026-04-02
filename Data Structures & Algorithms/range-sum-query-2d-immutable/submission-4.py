class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSum = [[0] * (len(matrix[0]) + 1) for r in range(len(matrix) + 1)]

        for i in range(len(matrix)):
            prefixSum = 0
            for j in range(len(matrix[0])):
                prefixSum += matrix[i][j]
                self.preSum[i + 1][j + 1] = prefixSum + self.preSum[i][j + 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.preSum[r2][c2]
        above = self.preSum[r1 - 1][c2]
        left = self.preSum[r2][c1 - 1]
        topLeft = self.preSum[r1 - 1][c1 - 1]

        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)