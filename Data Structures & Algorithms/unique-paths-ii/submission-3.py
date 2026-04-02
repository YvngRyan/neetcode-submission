class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dpGrid = [[0] * (n + 1) for i in range(m + 1)]

        dpGrid[m - 1][n - 1] = 1
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dpGrid[row][col] = 0
                else:
                    dpGrid[row][col] += dpGrid[row + 1][col] + dpGrid[row][col + 1]
        
        return dpGrid[0][0]