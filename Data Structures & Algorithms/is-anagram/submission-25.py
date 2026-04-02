class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMp = {}
        tMp = {}

        for i in range(len(s)):
            sMp[s[i]] = sMp.get(s[i], 0) + 1
            tMp[t[i]] = tMp.get(t[i], 0) + 1
        return sMp == tMp