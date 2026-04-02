class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #using sliding window technique, and keep track of
        #all the characters in the window using a set
        #continue increasing the window size as long as there
        #are no repeating characters in the set. If the next
        #iteration of the sliding window size increase causes
        #a duplicate, then increase the back of the sliding window
        #(Left pointer), and remove the character in corresponding
        #to the left pointer increase

        l, r = 0, 0
        
        characters = set()
        res = 0
        for r in range(len(s)):
            while s[r] in characters:
                characters.remove(s[l])
                l += 1
            characters.add(s[r])
            res = max(res, r - l + 1)
        return res

