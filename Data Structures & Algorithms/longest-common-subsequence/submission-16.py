class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def sub(t1, t2):
            if t1 == len(text1) or t2 == len(text2):
                return 0
            
            if (t1, t2) in cache:
                return cache[(t1, t2)]
            
            if text1[t1] == text2[t2]:
                cache[(t1, t2)] =  1 + sub(t1 + 1, t2 + 1)
            else:
                cache[(t1, t2)] = max(sub(t1 + 1, t2), sub(t1, t2 + 1))
            
            return cache[(t1, t2)]
        return sub(0, 0)