class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def subset(i, currSet):
            if i >= len(nums):
                res.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            subset(i + 1, currSet)
            currSet.pop()
            subset(i + 1, currSet)
        subset(0, [])
        return res