class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, combo, total):
            if i == len(nums) or total > target:
                return
            if total == target:
                res.append(combo.copy())
                return
            
            combo.append(nums[i])
            total += nums[i]
            dfs(i, combo, total)

            combo.pop()
            total -= nums[i]
            dfs(i + 1, combo, total)
        
        dfs(0, [], 0)
        return res