class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            elif c in closeToOpen:
                if not stack:
                    return False
                curr = stack.pop()
                if closeToOpen[c] != curr:
                    return False
        return not stack