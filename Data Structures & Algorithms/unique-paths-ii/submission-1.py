class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        cache = {}

        def search(row, col):
            if row >= m or col >= n:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == m - 1 and col == n - 1:
                return 1

            if (row, col) in cache:
                return cache[(row, col)]
            cache[(row, col)] = search(row + 1, col) + search(row, col + 1)

            return cache[(row, col)]
        return search(0, 0)
