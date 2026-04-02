class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1

        l, r = 0, 0
        currSum = 0
        while r < len(nums):
            currSum += nums[r]

            while currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1
            r += 1
        return res if res != len(nums) + 1 else 0