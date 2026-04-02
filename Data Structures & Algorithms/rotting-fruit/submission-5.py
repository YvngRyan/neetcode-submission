class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        totalFreshOranges = 0
        q = deque()
        minutes = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    totalFreshOranges += 1
                if grid[row][col] == 2:
                    q.append((row, col))
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while totalFreshOranges > 0 and q:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        totalFreshOranges -= 1
                        q.append((nx, ny))
            minutes += 1
            if totalFreshOranges == 0:
                return minutes
        return minutes if totalFreshOranges == 0 else -1

