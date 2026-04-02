class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def combo(i, currCombo):
            if len(currCombo) == k:
                res.append(currCombo.copy())
                return
            
            if i > n:
                return
            
            for j in range(i, n + 1):
                currCombo.append(j)
                combo(j + 1, currCombo)
                currCombo.pop()
        combo(1, [])
        return res