class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.trie = Trie()

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        