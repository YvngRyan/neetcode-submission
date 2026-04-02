class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N = len(grid), len(grid[0])

        q = collections.deque()
        dist = 0

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 0:
                    q.append((r, c))
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q:
            for i in range(len(q)):
                x, y = q.popleft()

                if grid[x][y] == 2147483647:
                    grid[x][y] = dist

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < M and ny >= 0 and ny < N and grid[nx][ny] == 2147483647:
                        q.append((nx, ny))
            dist += 1