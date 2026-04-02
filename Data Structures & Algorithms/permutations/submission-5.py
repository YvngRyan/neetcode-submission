class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i):
            if i >= len(nums):
                return [[]]
            
            resPerm = []
            perms = dfs(i + 1)

            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    resPerm.append(pCopy)
            return resPerm
        return dfs(0)