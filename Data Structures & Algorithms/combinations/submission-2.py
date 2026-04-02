class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, currCombo):
            if len(currCombo) == k:
                res.append(currCombo.copy())
                return
            if i > n:
                return
            
            currCombo.append(i)
            dfs(i + 1, currCombo)

            currCombo.pop()
            dfs(i + 1, currCombo)
        dfs(1, [])
        return res