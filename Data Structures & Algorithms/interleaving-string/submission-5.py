class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        def dfs(s1Idx, s2Idx, s3Idx):
            if (s1Idx, s2Idx, s3Idx) in cache:
                return cache[(s1Idx, s2Idx, s3Idx)]
            if s3Idx == len(s3):
                if s1Idx == len(s1) and s2Idx == len(s2):
                    return True
                return False

            cache[(s1Idx, s2Idx, s3Idx)] = False
            if s1Idx < len(s1) and s1[s1Idx] == s3[s3Idx] and s2Idx < len(s2) and s2[s2Idx] == s3[s3Idx]:
                cache[(s1Idx, s2Idx, s3Idx)] = dfs(s1Idx + 1, s2Idx, s3Idx + 1) or dfs(s1Idx, s2Idx + 1, s3Idx + 1)
            elif s1Idx < len(s1) and s1[s1Idx] == s3[s3Idx]:
                cache[(s1Idx, s2Idx, s3Idx)] = dfs(s1Idx + 1, s2Idx, s3Idx + 1)
            elif s2Idx < len(s2) and s2[s2Idx] == s3[s3Idx]:
                cache[(s1Idx, s2Idx, s3Idx)] =  dfs(s1Idx, s2Idx + 1, s3Idx + 1)
            
            return cache[(s1Idx, s2Idx, s3Idx)]
            
        return dfs(0, 0, 0)