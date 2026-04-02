class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tMap = {}
        sMap = {}
        for i in range(len(s)):
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
        return tMap == sMap

        