class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])

        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] not in node.children or (r, c) in visit:
                return
            
            word += board[r][c]
            node = node.children[board[r][c]]
            visit.add((r, c))

            if node.end:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
            
