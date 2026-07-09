class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op == "C":
                total -= stack[-1]
                stack.pop()
            elif op == "D":
                total += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif op == "+":
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
                total += int(op)
        
        return total