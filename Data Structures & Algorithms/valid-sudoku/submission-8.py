class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMp = {}
        colMp = {}
        squareMp = {}

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == ".":
                    continue

                if r not in rowMp:
                    rowMp[r] = set()
                if c not in colMp:
                    colMp[c] = set()
                
                square = (r // 3, c // 3)
                if square not in squareMp:
                    squareMp[square] = set()
                
                if num in rowMp[r] or num in colMp[c] or num in squareMp[square]:
                    return False
                
                rowMp[r].add(num)
                colMp[c].add(num)
                squareMp[square].add(num)
        return True
