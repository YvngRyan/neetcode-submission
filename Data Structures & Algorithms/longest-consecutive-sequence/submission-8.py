class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set()

        for n in nums:
            count.add(n)
        
        res = 0
        for n in nums:
            if n - 1 in count:
                continue
            curr = 0
            while n in count:
                curr += 1
                n += 1
            res = max(res, curr)
        return res