class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        
        need = len(count)

        l = 0
        have = 0
        curr = {}
        res, lowRes = [-1, -1], float("infinity")
        for r in range(len(s)):
            curr[s[r]] = curr.get(s[r], 0) + 1

            if s[r] in count and count[s[r]] == curr[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < lowRes:
                    res = [l, r]
                    lowRes = r - l + 1
                curr[s[l]] -= 1
                if s[l] in count and count[s[l]] == curr[s[l]] + 1:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if lowRes != float("infinity") else ""