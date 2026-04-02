class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def combo(i, currCombo):
            if len(currCombo) == k:
                res.append(currCombo.copy())
                return
            
            if i > n:
                return
            
            currCombo.append(i)
            combo(i + 1, currCombo)

            currCombo.pop()
            combo(i + 1, currCombo)
        combo(1, [])
        return res