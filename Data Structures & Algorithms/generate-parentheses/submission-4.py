class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def dfs(opened, closed):
            if opened == n and closed == n:
                res.append("".join(curr))
                return
            
            if opened < n:
                curr.append("(")
                dfs(opened + 1, closed)
                curr.pop()
            
            if closed < opened and closed < n:
                curr.append(")")
                dfs(opened, closed + 1)
                curr.pop()
        
        dfs(0, 0)
        return res