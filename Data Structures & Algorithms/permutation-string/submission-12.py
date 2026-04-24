class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Count = {}
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1

        s2Count = {}
        l = 0
        have = 0
        need = len(s1Count)
        for r in range(len(s2)):
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1
            if s2[r] in s1Count and s1Count[s2[r]] == s2Count[s2[r]]:
                have += 1
            
            while r - l + 1 > len(s1):
                if s2[l] in s1Count and s1Count[s2[l]] == s2Count[s2[l]]:
                    have -= 1
                s2Count[s2[l]] -= 1
                l += 1
            if have == need:
                return True
        return False