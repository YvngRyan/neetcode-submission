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
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        