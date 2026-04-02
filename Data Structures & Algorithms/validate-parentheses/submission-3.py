class Solution:
    def isValid(self, s: str) -> bool:
        # have a stack that inputs to the stack whenever it
        # goes over an open bracket. If facing a closed bracket,
        # and it doesn't match the open bracket at the top of the
        # stack, return false. If it does, continue
        # if we get to the end of the string and the stack isn't empty
        # return false
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
