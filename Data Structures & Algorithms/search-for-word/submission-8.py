class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r == len(board) or c < 0 or c == len(board[0]) or (r, c) in path or board[r][c] != word[i]:
                return False
            
            path.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True
            
            path.remove((r, c))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0): return True
        return False
