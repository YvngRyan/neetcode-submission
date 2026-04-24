class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                num2, num1 = stack.pop(), stack.pop()
                num3 = num2 + num1
                stack.append(num3)
            elif c == "-":
                num2, num1 = stack.pop(), stack.pop()
                num3 = num1 - num2
                stack.append(num3)
            elif c == "*":
                num2, num1 = stack.pop(), stack.pop()
                num3 = num1 * num2
                stack.append(num3)
            elif c == "/":
                num2, num1 = stack.pop(), stack.pop()
                num3 = int(num1 / num2)
                stack.append(num3)
            else:
                stack.append(int(c))
        return stack[0]