class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { "]" : "[", "}" : "{", ")" : "(" }

        stack = []

        for c in s:
            if c in closeToOpen:
                if not stack or stack.pop() != closeToOpen[c]:
                    return False
            else:
                stack.append(c)
        return False if stack else True