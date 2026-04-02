class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictionary = defaultdict(list)

        for s in strs:
            letter_count = [0] * 26

            for letter in s:
                letter_count[ord(letter) - ord("a")] += 1

            dictionary[tuple(letter_count)].append(s)
        return dictionary.values()

