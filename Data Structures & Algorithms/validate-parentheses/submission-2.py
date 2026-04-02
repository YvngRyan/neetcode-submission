class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}' : '{', ']' : '[' , ')' : '('}
        stack = []

        for c in s:
            if c not in mp.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                
                parentheses = stack.pop()
                if mp[c] != parentheses:
                    return False
        if stack:
            return False
        return True