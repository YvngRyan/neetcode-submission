class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total = 0
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax > rightMax:
                r -= 1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
            else:
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
        return total


        