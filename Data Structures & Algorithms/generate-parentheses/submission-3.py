class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opened, closed, curr):
            if opened == n and closed == n:
                res.append(curr)
                return
            
            if opened < n:
                dfs(opened + 1, closed, curr + "(")
            
            if closed < opened and closed < n:
                curr += ")"
                dfs(opened, closed + 1, curr)
        
        dfs(0, 0, "")
        return res