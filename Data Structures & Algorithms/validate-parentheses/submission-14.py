class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { "}" : "{", ")" : "(", "]" : "["}
        stack = []
        for c in s:
            if c in closeToOpen:
                if stack and stack.pop() == closeToOpen[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False