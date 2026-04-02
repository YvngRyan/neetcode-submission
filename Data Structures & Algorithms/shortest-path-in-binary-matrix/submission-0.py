class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        queue = collections.deque([(0, 0)])
        seen = set()
        seen.add((0, 0))
        length = 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                if row == n - 1 and col == n - 1:
                    return length
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr >= 0 and nr < n and nc >= 0 and nc < n and
                        (nr, nc) not in seen and grid[nr][nc] == 0):
                        queue.append((nr, nc))
                        seen.add((nr, nc))
            length += 1
        return -1
