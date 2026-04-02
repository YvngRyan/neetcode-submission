class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(r, c, node, word):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or board[r][c] not in node.children):
                return
            
            node = node.children[board[r][c]]
            visit.add((r, c))
            word += board[r][c]
            if node.end:
                res.add(word)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, node, word)
            
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
            
