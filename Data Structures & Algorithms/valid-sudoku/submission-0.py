class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                if num in rows[r] or num in columns[c] or num in squares[r // 3, c //3]:
                    return False
                columns[c].add(num)
                rows[r].add(num)
                squares[r // 3, c // 3].add(num)
        return True
        