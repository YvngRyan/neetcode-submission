class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def combo(i, currCombo, total):
            if total == target:
                res.append(currCombo.copy())
                return
            if total > target:
                return
            if i >= len(nums):
                return
            
            currCombo.append(nums[i])
            total += nums[i]
            combo(i, currCombo, total)
            currCombo.pop()
            total -= nums[i]
            combo(i + 1, currCombo, total)
        combo(0, [], 0)
        return res