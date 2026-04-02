class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Count, s2Count = {}, {}

        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1

        for r in range(len(s1)):
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1
        
        l = 0

        for r in range(len(s1), len(s2)):
            if s2Count == s1Count: return True
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1
            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]]
            l += 1
        return s2Count == s1Count
        