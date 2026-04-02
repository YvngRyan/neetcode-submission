class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def perm(i):
            if i == len(nums):
                return [[]]
            
            perms = perm(i + 1)
            n = nums[i]
            newPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    newPerms.append(pCopy)
            return newPerms
        
        return perm(0)