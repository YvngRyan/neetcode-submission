class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combo, currSum):
            if i == len(nums):
                if currSum == target:
                    res.append(combo.copy())
                return
            
            if currSum > target:
                return
            
            combo.append(nums[i])
            currSum += nums[i]
            dfs(i, combo, currSum)

            combo.pop()
            currSum -= nums[i]

            dfs(i + 1, combo, currSum)
        dfs(0, [], 0)
        return res