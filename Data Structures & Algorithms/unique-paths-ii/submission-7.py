class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0

        prevRow = [0] * COLS
        prevRow[-1] = 1
        for row in range(ROWS - 1, -1, -1):
            currRow = [0] * COLS
            for col in range(COLS - 1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    currRow[col] = 0
                else:
                    rightVal = 0 if col == COLS - 1 else currRow[col + 1]
                    currRow[col] = prevRow[col] + rightVal
            prevRow = currRow
        return prevRow[0]