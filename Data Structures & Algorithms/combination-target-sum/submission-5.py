class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def combo(i, currCombo, total):
            if total == target:
                res.append(currCombo.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            currCombo.append(nums[i])
            combo(i, currCombo, total + nums[i])

            currCombo.pop()
            combo(i + 1, currCombo, total)
        
        combo(0, [], 0)
        return res