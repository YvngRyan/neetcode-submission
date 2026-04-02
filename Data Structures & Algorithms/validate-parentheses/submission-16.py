class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { "]" : "[", "}" : "{", ")" : "(" }

        stack = []

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if not stack or stack.pop() != closeToOpen[c]:
                    return False
        return not stack