class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSumCnt = { 0 : 1 }


        res = 0
        preSum = 0
        for num in nums:
            preSum += num
            
            if preSum - k in prefSumCnt:
                res += prefSumCnt[preSum - k]
            prefSumCnt[preSum] = prefSumCnt.get(preSum, 0) + 1
            
        return res
