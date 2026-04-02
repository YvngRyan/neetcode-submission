class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Check the column
        #Create a Map with values of a set, and then go through the column and add the value to the column set
        
        #Check the row
        #Create a Map with the values of a set, and then go through the row and add the value to the row set

        #Check the box
        #Create a Map with the values of a set, and then do // operator to see which box it belongs to
        colMap = defaultdict(set)
        rowMap = defaultdict(set)
        boxMap = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in colMap[j]
                    or board[i][j] in rowMap[i]
                    or board[i][j] in boxMap[(i // 3, j // 3)]):
                    return False
                else:
                    colMap[j].add(board[i][j])
                    rowMap[i].add(board[i][j])
                    boxMap[(i // 3, j // 3)].add(board[i][j])
        return True
                
