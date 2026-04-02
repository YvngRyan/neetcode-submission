class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            currRes = []
            for perm in res:
                for i in range(len(perm) + 1):
                    permCopy = perm.copy()
                    permCopy.insert(i, n)
                    currRes.append(permCopy)
            res = currRes
        return res
