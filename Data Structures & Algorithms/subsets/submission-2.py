class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def dfs(i, subSet):
            if i >= len(nums):
                return

            subSet.append(nums[i])
            dfs(i + 1, subSet)
            res.append(subSet.copy())

            subSet.remove(nums[i])
            dfs(i + 1, subSet)

        dfs(0, [])
        return res