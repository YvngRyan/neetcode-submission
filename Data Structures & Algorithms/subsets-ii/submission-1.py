class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, currSub):
            if i == len(nums):
                res.append(currSub.copy())
                return
            
            currSub.append(nums[i])
            dfs(i + 1, currSub)

            currSub.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, currSub)
        dfs(0, [])
        return res