class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        currTotal = 0
        for r in range(len(nums)):
            currTotal += nums[r]

            while currTotal >= target:
                res = min(r - l + 1, res)
                currTotal -= nums[l]
                l += 1
        return res if res != float('inf') else 0