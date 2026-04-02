class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, currSum, combo):
            if i >= len(nums) or currSum > target:
                return
            if currSum == target:
                res.append(combo.copy())
                return

            currSum += nums[i]
            combo.append(nums[i])
            dfs(i, currSum, combo)

            combo.pop()
            currSum -= nums[i]
            dfs(i + 1, currSum, combo)
        dfs(0, 0, [])
        return res