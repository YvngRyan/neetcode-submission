class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2Mp = {}
        s1Mp = {}

        for c in s1:
            s1Mp[c] = s1Mp.get(c, 0) + 1
        
        need = len(s1Mp)

        have = 0

        l = 0
        for r in range(len(s2)):
            s2Mp[s2[r]] = s2Mp.get(s2[r], 0) + 1

            if s2[r] in s1Mp and s1Mp[s2[r]] == s2Mp[s2[r]]:
                have += 1
            
            # if s2[r] in s1Mp and s1Mp[s2[r]] == s2Mp[s2[r]] - 1:
            #     have -= 1

            while r - l + 1 > len(s1):
                s2Mp[s2[l]] -= 1
                if s2[l] in s1Mp and s1Mp[s2[l]] == s2Mp[s2[l]] + 1:
                    have -= 1
                l += 1
            
            if have == need:
                return True
            
        return False