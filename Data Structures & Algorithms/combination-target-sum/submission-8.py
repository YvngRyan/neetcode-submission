class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def combo(i, currCombo, currTotal):
            if currTotal == target:
                res.append(currCombo.copy())
                return
            
            if currTotal > target or i == len(nums):
                return
            
            currCombo.append(nums[i])
            currTotal += nums[i]
            combo(i, currCombo, currTotal)

            currCombo.pop()
            currTotal -= nums[i]
            combo(i + 1, currCombo, currTotal)
        
        combo(0, [], 0)
        return res
