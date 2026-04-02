class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        topRow, bottomRow = 0, rows - 1

        while topRow <= bottomRow:
            midRow = (topRow + bottomRow) // 2
            if target > matrix[midRow][-1]:
                topRow = midRow + 1
            elif target < matrix[midRow][0]:
                bottomRow = midRow - 1
            else:
                break
        if not (topRow <= bottomRow): return False

        row = (topRow + bottomRow) // 2
        l, r = 0, columns - 1

        while l <= r:
            mid = (r + l) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False
            