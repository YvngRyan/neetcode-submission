class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            currPerms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    permCopy = perm.copy()
                    permCopy.insert(i, n)
                    currPerms.append(permCopy)
            perms = currPerms
        return perms