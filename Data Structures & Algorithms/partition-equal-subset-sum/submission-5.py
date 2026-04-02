class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        target = total // 2

        for i in range(len(nums)):
            newDp = set()
            for n in dp:
                if (n + nums[i]) == target:
                    return True
                newDp.add(n + nums[i])
                newDp.add(n)
            dp = newDp
        
        return False