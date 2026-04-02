class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCount = defaultdict(set)
        colCount = defaultdict(set)
        squareCount = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rowCount[row]
                    or board[row][col] in colCount[col]
                    or board[row][col] in squareCount[(row // 3, col // 3)]):
                    return False
                rowCount[row].add(board[row][col])
                colCount[col].add(board[row][col])
                squareCount[(row // 3, col // 3)].add(board[row][col])
        return True