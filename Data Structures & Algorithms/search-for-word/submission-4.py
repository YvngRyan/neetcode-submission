class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def search(r, c, curIdx):
            if board[r][c] != word[curIdx]:
                return False
            if curIdx == len(word) - 1:
                return True
            
            path.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) 
                        and (nr, nc) not in path):
                    if search(nr, nc, curIdx + 1):
                        return True
            path.remove((r, c))
            return False


        path = set()
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if search(r, c, 0):
                    return True
        return False