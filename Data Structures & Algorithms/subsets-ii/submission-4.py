class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        def dfs(i, sub, total):
            if i == len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            total += nums[i]
            dfs(i + 1, sub, total)

            sub.pop()
            total -= nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, sub, total)
        dfs(0, [], 0)
        return res