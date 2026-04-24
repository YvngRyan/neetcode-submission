class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        path = 1
        q = collections.deque([(0, 0)])
        seen = set()

        while q:
            currLength = len(q)
            for i in range(currLength):
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return path
                
                seen.add((r, c))
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (nr < 0 or nr == len(grid) or nc < 0 or nc == len(grid[0]) or (nr, nc) in seen or grid[nr][nc] == 1):
                        q.append((nr, nc))
                
            path += 1
        return -1