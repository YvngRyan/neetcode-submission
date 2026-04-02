class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (height, idx)

        for i in range(len(heights)):
            h = heights[i]

            lastIdx = float("inf")
            while stack and stack[-1][0] > h:
                area = stack[-1][0] * (i - stack[-1][1])
                maxArea = max(maxArea, area)
                lastIdx = stack[-1][1]
                stack.pop()
            
            stack.append((h, min(lastIdx, i)))
        
        while stack:
            area = stack[-1][0] * (len(heights) - stack[-1][1])
            maxArea = max(maxArea, area)
            stack.pop()
        return maxArea


        # stack = [(1, 0)]
        # heights = [7, 1, 7, 2, 2, 4]

        # h = 4
        # i = 5
        # lastIdx = inf
        # area = 1 * 6 = 6

        # maxArea = 8
