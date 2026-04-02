class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        cache = {}
        def dfs(w1Idx, w2Idx):
            if (w1Idx, w2Idx) in cache:
                return cache[(w1Idx, w2Idx)]
            if w2Idx == len(word2):
                return len(word1) - w1Idx  
            if w1Idx == len(word1):
                return len(word2) - w2Idx

            cache[(w1Idx, w2Idx)] = 0
            if word1[w1Idx] == word2[w2Idx]:
                cache[(w1Idx, w2Idx)] = dfs(w1Idx + 1, w2Idx + 1)
            else:
                # Delete (emulate), Insert (emulate), Replace
                cache[(w1Idx, w2Idx)] = min(1 + dfs(w1Idx + 1, w2Idx),
                            1 + dfs(w1Idx, w2Idx + 1),
                            1 + dfs(w1Idx + 1, w2Idx + 1))
            return cache[(w1Idx, w2Idx)]
            
        return dfs(0, 0)