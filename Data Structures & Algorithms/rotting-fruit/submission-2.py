class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])

        q = collections.deque()
        visited = set()
        minutes = 0
        fresh = 0

        # Loop through the grid and add all initial rotten fruits to the q
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        #Run bfs on the rotten fruits
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nr < rows and nc >= 0 and nc < columns and
                        (nr, nc) not in visited and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1