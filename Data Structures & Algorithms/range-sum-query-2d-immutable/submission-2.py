class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixMatrix = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        for row in range(len(matrix)):
            prefixSum = 0
            for col in range(len(matrix[0])):
                prefixSum += matrix[row][col]
                above = self.prefixMatrix[row][col + 1]
                self.prefixMatrix[row + 1][col + 1] = prefixSum + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefixMatrix[r2][c2]
        topSubtract = self.prefixMatrix[r1 - 1][c2]
        leftSubtract = self.prefixMatrix[r2][c1 - 1]
        topLeftAdd = self.prefixMatrix[r1 - 1][c1 - 1]

        return bottomRight + topLeftAdd - topSubtract - leftSubtract

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)