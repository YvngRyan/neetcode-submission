class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aMp = defaultdict(list)

        for s in strs:
            ptn = [0] * 26
            for c in s:
                ptn[ord(c) - ord('a')] += 1
            aMp[tuple(ptn)].append(s)
        
        return list(aMp.values())