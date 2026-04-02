class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(i, curr):
            if i == len(word):
                return curr.end
            
            if word[i] == ".":
                for child in curr.children.values():
                    if dfs(i + 1, child): return True
                return False
            
            if word[i] in curr.children:
                return dfs(i + 1, curr.children[word[i]])
            
            return False
        
        return dfs(0, self.trie)