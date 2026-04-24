class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        
        for n in range(len(nums)):
            ans[n] = ans[len(nums) + n] = nums[n]
        return ans