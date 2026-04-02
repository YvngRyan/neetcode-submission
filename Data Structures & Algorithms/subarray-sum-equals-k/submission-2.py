class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prevSums = { 0 : 1 }
        prefixSum = 0
        res = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            diff = prefixSum - k
            if diff in prevSums:
                res += prevSums[diff]
            prevSums[prefixSum] = prevSums.get(prefixSum, 0) + 1
        return res
        