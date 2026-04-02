class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            m = (top + bottom) // 2
            row = matrix[m]
            if row[0] > target:
                bottom = m - 1
            elif row[-1] < target:
                top = m + 1
            else:
                break
        if top > bottom:
            return False
        
        row = (top + bottom) // 2
        l, r = 0, cols - 1

        while l <= r:
            m = (r + l) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
        