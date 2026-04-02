class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tMap, sMap = {}, {}

        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        need = len(tMap)
        have = 0
        l = 0
        res, resLength = [-1, -1], float("infinity")
        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            if s[r] in tMap and tMap[s[r]] == sMap[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < resLength:
                    resLength = r - l + 1
                    res = [l, r]

                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLength != float("infinity") else ""

