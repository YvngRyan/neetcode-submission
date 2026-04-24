class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        

        have = 0
        need = len(tCount)
        sCount = {}

        res = ""

        l = 0
        for r in range(len(s)):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            if s[r] in tCount and tCount[s[r]] == sCount[s[r]]:
                have += 1
            
            while have == need:
                if res == "" or len(res) > (r - l + 1):
                    res = s[l:r + 1]
                
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] == tCount[s[l]] - 1:
                    have -= 1
                l += 1
        return res