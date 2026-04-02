class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = []
        res = []

        def backtrack(openP, closeP):
            if openP == n and closeP == n:
                res.append("".join(curr))
                return
            
            if openP < n:
                curr.append("(")
                backtrack(openP + 1, closeP)
                curr.pop()
            
            if closeP < openP:
                curr.append(")")
                backtrack(openP, closeP + 1)
                curr.pop()
            
        backtrack(0, 0)
        return res