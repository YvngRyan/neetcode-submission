class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for n in nums:
            cnt = cnt + 1 if n == 1 else 0
            res = max(cnt, res)
        return res