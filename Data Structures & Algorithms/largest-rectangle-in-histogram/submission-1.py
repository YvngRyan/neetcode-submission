class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i in range(len(heights)):
            h = heights[i]

            prevIdx = i
            while stack and stack[-1][0] > h:
                prevH, prevI = stack.pop()
                area = prevH * (i - prevI)
                maxArea = max(area, maxArea)
                prevIdx = prevI
            
            stack.append((h, prevIdx))

        while stack:
            h, i = stack.pop()
            area = h * (len(heights) - i)
            maxArea = max(area, maxArea)
        return maxArea

