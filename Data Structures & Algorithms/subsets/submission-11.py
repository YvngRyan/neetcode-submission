class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        for i in range(1 << n):
            currSub = []
            for j in range(n):
                if (i & 1 << j):
                    currSub.append(nums[j])
            res.append(currSub.copy())
        return res