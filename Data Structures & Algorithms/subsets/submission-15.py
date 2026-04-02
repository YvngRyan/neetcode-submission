class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            for i in range(len(res)):
                newSubset = res[i] + [num]
                res.append(newSubset)
        
        return res