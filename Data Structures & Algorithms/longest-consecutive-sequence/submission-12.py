class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set()
        for n in nums:
            count.add(n)

        res = 0
        for n in nums:
            curr = 1
            if n - 1 not in count:
                while n + curr in count:
                    curr += 1
            res = max(curr, res)
        return res