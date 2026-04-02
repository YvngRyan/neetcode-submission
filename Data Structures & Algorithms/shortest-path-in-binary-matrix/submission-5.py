class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
        if grid[0][0] == 1 or grid[ROWS][COLS] == 1:
            return -1

        q = collections.deque([(0, 0)])
        grid[0][0] = 1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

        lvl = 1
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                if x == ROWS and y == COLS:
                    return lvl
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx <= ROWS and ny >= 0 and ny <= COLS and grid[nx][ny] == 0:
                        q.append((nx, ny))
                        grid[nx][ny] = 1
            lvl += 1
        return -1