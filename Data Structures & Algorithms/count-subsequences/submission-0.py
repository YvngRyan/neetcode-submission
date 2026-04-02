class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(sIdx, tIdx):
            if tIdx == len(t):
                return 1
            if sIdx == len(s):
                return 0

            # Take this letter (if it matches the letter in "t")
            # Don't take this letter (even if it matches), and continue dfs
            numsSub = 0
            if s[sIdx] == t[tIdx]:
                numsSub += dfs(sIdx + 1, tIdx + 1) + dfs(sIdx + 1, tIdx)
            else:
                numsSub += dfs(sIdx + 1, tIdx)
            
            return numsSub
        
        return dfs(0, 0)