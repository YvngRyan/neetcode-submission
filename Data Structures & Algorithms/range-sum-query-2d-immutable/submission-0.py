class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * len(matrix[0]) for i in range(len(matrix))]

        for row in range(len(matrix)):
            prefixSum = 0
            for col in range(len(matrix[row])):
                prefixSum += matrix[row][col]
                self.prefix[row][col] = prefixSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            subPrefix = 0
            if col1 != 0:
                subPrefix = self.prefix[row][col1 - 1]
            currSum = self.prefix[row][col2] - subPrefix
            res += currSum
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)