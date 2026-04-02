class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colMp = {}
        rowMp = {}
        boxMp = {}

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                
                if c not in colMp:
                    colMp[c] = set()

                if board[r][c] in colMp[c]:
                    return False
                colMp[c].add(board[r][c])

                if r not in rowMp:
                    rowMp[r] = set()

                if board[r][c] in rowMp[r]:
                    return False
                rowMp[r].add(board[r][c])

                if (r // 3, c // 3) not in boxMp:
                    boxMp[(r // 3, c // 3)] = set()
                
                if board[r][c] in boxMp[(r // 3, c // 3)]:
                    return False
                boxMp[(r // 3, c // 3)].add(board[r][c])
        return True