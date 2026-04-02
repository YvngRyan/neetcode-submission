class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, tmp in enumerate(temperatures):
            while stack and stack[-1][0] < tmp:
                sTmp, sIdx = stack.pop()
                res[sIdx] = i - sIdx
            stack.append((tmp, i))
        return res