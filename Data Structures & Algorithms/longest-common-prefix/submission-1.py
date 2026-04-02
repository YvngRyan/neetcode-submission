class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for i in range(len(strs) - 1):
            s1, s2 = strs[i], strs[i + 1]
            if i + 1 < len(strs):
                s2 = strs[i + 1]
            
            count = 0
            i1, i2 = 0, 0
            while i1 < len(s1) and i2 < len(s2):
                if s1[i1] == s2[i2]:
                    count += 1
                else:
                    break
                i1 += 1
                i2 += 1
            if count <= len(longest):
                longest = s1[:count]
        return longest