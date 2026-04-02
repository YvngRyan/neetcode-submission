class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        maxLeft[0] = height[0]
        maxRight[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])

        for i in range(len(height)):
            minDiff = min(maxLeft[i], maxRight[i])
            diff = minDiff - height[i]
            res += (max(0, diff))
        return res




        