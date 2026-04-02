class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for words in strs:
            count = [0] * 26
            for letter in words:
                count[ord(letter) - ord('a')] += 1
            res[tuple(count)].append(words)
        return list(res.values())
        