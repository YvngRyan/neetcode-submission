class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def combination(i, currCombo):
            if len(currCombo) >= k:
                res.append(currCombo.copy())
                return
            if i > n:
                return
            
            currCombo.append(i)
            combination(i + 1, currCombo)
            currCombo.pop()
            combination(i + 1, currCombo)
        combination(1, [])
        return res