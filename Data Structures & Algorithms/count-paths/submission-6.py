class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for row in range(m - 1, -1, -1):
            currRow = [0] * n
            currRow[-1] = 1
            for col in range(n - 2, -1, -1):
                currRow[col] = currRow[col + 1] + prevRow[col]
            prevRow = currRow
        return prevRow[0]