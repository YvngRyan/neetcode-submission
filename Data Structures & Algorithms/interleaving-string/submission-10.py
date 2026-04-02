class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        def dfs(s1Idx, s2Idx):
            if (s1Idx, s2Idx) in cache:
                return cache[(s1Idx, s2Idx)]
            if s1Idx + s2Idx == len(s3):
                return s1Idx == len(s1) and s2Idx == len(s2)

            cache[(s1Idx, s2Idx)] = False
            if s1Idx < len(s1) and s1[s1Idx] == s3[s1Idx + s2Idx] and s2Idx < len(s2) and s2[s2Idx] == s3[s1Idx + s2Idx]:
                cache[(s1Idx, s2Idx)] = dfs(s1Idx + 1, s2Idx) or dfs(s1Idx, s2Idx + 1)
            elif s1Idx < len(s1) and s1[s1Idx] == s3[s1Idx + s2Idx]:
                cache[(s1Idx, s2Idx)] = dfs(s1Idx + 1, s2Idx)
            elif s2Idx < len(s2) and s2[s2Idx] == s3[s1Idx + s2Idx]:
                cache[(s1Idx, s2Idx)] =  dfs(s1Idx, s2Idx + 1)
            
            return cache[(s1Idx, s2Idx)]
            
        return dfs(0, 0)