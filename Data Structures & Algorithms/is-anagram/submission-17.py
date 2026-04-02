class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mpS = {}
        mpT = {}
        for i in range(len(s)):
            mpS[s[i]] = mpS.get(s[i], 0) + 1
            mpT[t[i]] = mpT.get(t[i], 0) + 1
        return mpS == mpT