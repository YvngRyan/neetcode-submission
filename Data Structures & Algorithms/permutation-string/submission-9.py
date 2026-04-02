class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Mp = {}
        for c in s1:
            s1Mp[c] = s1Mp.get(c, 0) + 1
        
        need = len(s1Mp)

        have = 0
        s2Mp = {}
        l, r = 0, 0
        while r < len(s2):
            s2Mp[s2[r]] = s2Mp.get(s2[r], 0) + 1
            if s2[r] in s1Mp:
                if s2Mp[s2[r]] == s1Mp[s2[r]]:
                    have += 1
                elif s2Mp[s2[r]] == s1Mp[s2[r]] + 1:
                    have -= 1
                

            if r - l + 1 > len(s1):
                s2Mp[s2[l]] -= 1
                if s2[l] in s1Mp:
                    if s2Mp[s2[l]] == s1Mp[s2[l]] - 1:
                        have -= 1
                    elif s2Mp[s2[l]] == s1Mp[s2[l]]:
                        have += 1
                l += 1
            r += 1
            if have == need:
                return True
        return False
