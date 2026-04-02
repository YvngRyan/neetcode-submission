class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Unique Path if you reach row == m - 1 and col = n - 1
        # Only Moves Allowed: Down = row - 1, Right = col + 1
        # prevRow = [1] * n

        # for row in range(m - 2, -1, -1):
        #     currRow = [0] * n
        #     currRow[-1] = 1
        #     for col in range(n - 2, -1, -1):
        #         currRow[col] = currRow[col + 1] + prevRow[col]

        #     prevRow = currRow
        
        # return prevRow[0]

        dp = [[0] * (n + 1) for i in range(m + 1)]
        dp[m][n - 1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
        return dp[0][0]