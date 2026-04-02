class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currCombo, total):
            if total == target:
                res.append(currCombo.copy())
                return
            if i == len(nums) or total > target:
                return
            
            currCombo.append(nums[i])
            total += nums[i]
            dfs(i, currCombo, total)

            currCombo.pop()
            total -= nums[i]
            dfs(i + 1, currCombo, total)
        dfs(0, [], 0)
        return res