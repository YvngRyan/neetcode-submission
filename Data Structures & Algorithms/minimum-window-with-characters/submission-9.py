class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""
        
        tMp = defaultdict(int)
        for c in t:
            tMp[c] += 1


        sMp = defaultdict(int)
        need = len(tMp)
        have = 0
        l = 0

        res = ""
        for r in range(len(s)):
            sMp[s[r]] += 1

            if s[r] in tMp and tMp[s[r]] == sMp[s[r]]:
                have += 1
            
            while have == need:
                if res == "" or len(res) > r - l + 1:
                    res = s[l : r + 1]
                sMp[s[l]] -= 1
                if s[l] in tMp and tMp[s[l]] == sMp[s[l]] + 1:
                    have -= 1
                l += 1
        return res