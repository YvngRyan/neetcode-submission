class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            cur = node

            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if c in cur.children:
                        cur = cur.children[c]
                    else:
                        return False
            return cur.end
        
        return dfs(0, self.root)

        #day, bay, may