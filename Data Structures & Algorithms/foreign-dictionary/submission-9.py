class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = { c : [] for w in words for c in w }
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if not self.compWords(w1, w2, adjList):
                return ""

        visit = set()
        path = set()
        res = ""

        def dfs(c):
            nonlocal res
            if c in visit:
                return True
            if c in path:
                return False

            path.add(c)

            for neigh in adjList[c]:
                if not dfs(neigh):
                    return False

            path.remove(c)
            visit.add(c)
            res += c
            return True

        for c in adjList.keys():
            if not dfs(c):
                return ""
        return res[::-1]
    def compWords(self, w1, w2, adjList):
        i = 0
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return False

        for i in range(minLen):
            if w1[i] != w2[i]:
                adjList[w1[i]].append(w2[i])
                break
        return True