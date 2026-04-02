class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0:
            return False
        bRow, tRow = 0, len(matrix) - 1

        row = None
        while bRow <= tRow:
            mRow = (bRow + tRow) // 2
            if target < matrix[mRow][0]:
                tRow = mRow - 1
            elif target > matrix[mRow][-1]:
                bRow = mRow + 1
            else:
                break

        if not (bRow <= tRow):
            return False
        
        row = (bRow + tRow) // 2
        
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (r + l) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False