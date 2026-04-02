class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = set(nums)

        res = 0
        for n in nums:
            if (n - 1) in nums:
                continue
            
            m = n
            while m in cnt:
                m += 1
            res = max(res, m - n)
        return res