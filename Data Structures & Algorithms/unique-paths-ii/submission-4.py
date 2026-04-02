class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        prevRow = [0] * (n + 1)
        prevRow[-2] = 1
        
        for row in range(m - 1, -1, -1):
            currRow = [0] * (n + 1)
            for col in range(n - 1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    continue
                else:
                    currRow[col] += currRow[col + 1] + prevRow[col]
            prevRow = currRow
        return currRow[0]