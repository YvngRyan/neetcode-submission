class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(sIdx, tIdx):
            if tIdx == len(t):
                return 1
            if sIdx == len(s):
                return 0

            if (sIdx, tIdx) in cache:
                return cache[(sIdx, tIdx)]

            # Take this letter (if it matches the letter in "t")
            # Don't take this letter (even if it matches), and continue dfs
            cache[(sIdx, tIdx)] = 0
            if s[sIdx] == t[tIdx]:
                cache[(sIdx, tIdx)] += dfs(sIdx + 1, tIdx + 1) + dfs(sIdx + 1, tIdx)
            else:
                cache[(sIdx, tIdx)] += dfs(sIdx + 1, tIdx)
            
            return cache[(sIdx, tIdx)]
        
        return dfs(0, 0)