class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        pacific = set()

        pQ = collections.deque()

        # Add Initial cells touching Pacific
        for i in range(m):
            pQ.append((0, i))
        for i in range(1, n):
            pQ.append((i, 0))

        while pQ:
            for i in range(len(pQ)):
                r, c = pQ.popleft()

                if (r, c) in pacific:
                    continue
                
                pacific.add((r, c))
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c 
                    if (nr >= 0 and nr < n and nc >= 0 and nc < m 
                        and (nr, nc) not in pacific and heights[nr][nc] >= heights[r][c]):
                        pQ.append((nr, nc))
        
        aQ = collections.deque()
        atlantic = set()

        # Add initial cells touching Atlantic
        for i in range(m):
            aQ.append((n - 1, i))
        for i in range(n):
            aQ.append((i, m - 1))
        
        res = []
        while aQ:
            for i in range(len(aQ)):
                r, c = aQ.popleft()

                if (r, c) in atlantic:
                    continue
                
                atlantic.add((r, c))
                if (r, c) in pacific:
                    res.append([r, c])

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c 
                    if (nr >= 0 and nr < n and nc >= 0 and nc < m and (nr, nc) not in atlantic and heights[nr][nc] >= heights[r][c]):
                        aQ.append((nr, nc))
        return res