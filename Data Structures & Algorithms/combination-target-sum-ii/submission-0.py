class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            combo.append(candidates[i])
            dfs(i + 1, combo, total + candidates[i])

            combo.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1

            dfs(i + 1, combo, total)
        dfs(0, [], 0)
        return res