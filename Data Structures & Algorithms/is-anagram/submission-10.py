class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) != len(t):
            return False
        
        setS = {}
        setT = {}
        for l in range(len(s)):
            setS[s[l]] = setS.get(s[l], 0) + 1
            setT[t[l]] = setT.get(t[l], 0) + 1
        
        return setT == setS