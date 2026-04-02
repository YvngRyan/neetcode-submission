class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, currCombo):
            if len(currCombo) == k:
                res.append(currCombo.copy())
                return
            if i > n:
                return
            
            for j in range(i, n + 1):
                currCombo.append(j)
                dfs(j + 1, currCombo)
                currCombo.pop()
        dfs(1, [])
        return res