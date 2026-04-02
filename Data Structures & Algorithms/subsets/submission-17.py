class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            for i in range(len(res)):
                subCopy = res[i].copy()
                subCopy.append(n)
                res.append(subCopy)
        return res