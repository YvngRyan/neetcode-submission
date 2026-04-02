class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, currSum, combo):
            if i >= len(nums) or currSum > target:
                return
            if currSum == target:
                res.append(combo.copy())
                return

            currSum += nums[i]
            combo.append(nums[i])
            dfs(i, currSum, combo)

            combo.pop()
            currSum -= nums[i]
            dfs(i + 1, currSum, combo)
        dfs(0, 0, [])
        return res

        # (0, 2, [2]) -> (0, 4, [2. 2]) -> (0, 6, [2, 2, 2]) -> (0, 8, [2, 2, 2, 2]) -> (0, 10, [2, 2, 2, 2, 2])
        #                                                                            -> (1, 13, [2, 2, 2, 2, 5])
        #                                                    -> (1, 11, [2, 2, 2, 5])
        #                               -> (1, 9, [2, 2, 5]))
        #             -> (1, 5, [5])