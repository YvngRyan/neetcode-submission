class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lRow, rRow = 0, len(matrix) - 1

        row = None
        while lRow <= rRow:
            mRow = (lRow + rRow) // 2

            if matrix[mRow][0] > target:
                rRow = mRow - 1
            elif matrix[mRow][-1] < target:
                lRow = mRow + 1
            else:
                row = mRow
                break
        
        if row == None:
            return False
        
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            
            if matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False