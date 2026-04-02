class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            newIdx = i
            while stack and stack[-1][0] > h:
                h1, i2 = stack.pop()
                res = max(res, h1 * (i - i2))
                newIdx = i2
            stack.append((h, newIdx))
        
        while stack:
            h, i = stack.pop()
            res = max(res, h * (len(heights) - i))
        return res