class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]" : "[", ")" : "(", "}" : "{"}
        stack = []

        for c in s:
            if c in closeToOpen:
                if not (stack and stack[-1] == closeToOpen[c]):
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
