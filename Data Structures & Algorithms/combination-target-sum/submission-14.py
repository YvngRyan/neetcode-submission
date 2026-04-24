class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total):
            if total > target:
                return
            if i == len(nums):
                if total == target:
                    res.append(curr.copy())
                return
            
            curr.append(nums[i])
            total += nums[i]
            dfs(i, curr, total)

            curr.pop()
            total -= nums[i]

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return res