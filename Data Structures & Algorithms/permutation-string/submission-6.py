class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        need = len(count1)
        for i in range(len(s2)):
            count2 = {}
            cur = 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1
                if count2[s2[j]] == count1.get(s2[j], 0):
                    cur += 1
                if count2[s2[j]] > count1.get(s2[j], 0):
                    break
                if cur == need:
                    return True
        return False