class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c not in col and (r - c) not in negDiag and (r + c) not in posDiag:
                    col.add(c)
                    negDiag.add(r - c)
                    posDiag.add(r + c)
                    board[r][c] = "Q"
                    dfs(r + 1)
                    col.remove(c)
                    negDiag.remove(r - c)
                    posDiag.remove(r + c)
                    board[r][c] = "."
        
        dfs(0)
        return res