class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Unique Path if you reach row == m - 1 and col = n - 1
        # Only Moves Allowed: Down = row - 1, Right = col + 1

        #HashMap that contains key = (row, col) -> val = (number of ways from (row, col) that reach bottom-right)
        cache = {}

        def path(row, col):
            if row >= m or col >= n:
                return 0
            if row == m - 1 and col == n - 1:
                return 1

            if (row, col) in cache:
                return cache[(row, col)]

            cache[(row, col)] = path(row + 1, col) + path(row, col + 1)

            return cache[(row, col)]
        return path(0, 0)