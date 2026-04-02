class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # Check if top left or bottom right is invalid
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1
        
        q = collections.deque([(0, 0, 1)])
        visit = set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        while q:
            r, c, lvl = q.popleft()

            visit.add((r, c))

            if r == N - 1 and c == N - 1:
                return lvl
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < N and nc >= 0 and nc < N and grid[nr][nc] == 0 and (nr, nc) not in visit:
                    q.append((nr, nc, lvl + 1))
        
        return -1