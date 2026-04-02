class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tRow, bRow = 0, len(matrix) - 1

        row = None
        while tRow <= bRow:
            mRow = (tRow + bRow) // 2
            
            if matrix[mRow][0] > target:
                bRow = mRow - 1
            elif matrix[mRow][-1] < target:
                tRow = mRow + 1
            else:
                row = mRow
                break
        
        if row == None:
            return False
        
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False