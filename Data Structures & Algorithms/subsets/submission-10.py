class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, currSub):
            if i == len(nums):
                res.append(currSub.copy())
                return
            
            currSub.append(nums[i])
            dfs(i + 1, currSub)

            currSub.pop()
            dfs(i + 1, currSub)

        dfs(0, [])
        return res