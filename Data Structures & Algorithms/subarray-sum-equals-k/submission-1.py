class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0 : 1}
        res = 0

        prefix = 0
        for num in nums:
            prefix += num
            if (prefix - k) in mp:
                res += mp[prefix-k]
            
            mp[prefix] = mp.get(prefix, 0) + 1
        
        return res
