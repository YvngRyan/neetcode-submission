class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N = len(grid), len(grid[0])

        # queue: BFS
        # queue= [(x, y, (original land coordinate))]
        # if x, y = 0 (treasure), then mark the original land coordinate as the distance
        # Can keep track of distance by an outside variable, incremented everytime we do one round
        # Of BFS
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