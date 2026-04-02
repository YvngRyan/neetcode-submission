class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(i):
            if i == len(nums):
                return [[]]
            
            perms = dfs(i + 1)

            newPerms = []
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    newPerms.append(pCopy)
            return newPerms
        return dfs(0)