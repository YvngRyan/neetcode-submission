class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        leftMax = 0
        rightMax = 0
        
        totalWater = 0
        while l <= r:
            if leftMax <= rightMax:
                totalWater += max(0, leftMax - height[l])
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                totalWater += max(0, rightMax - height[r])
                rightMax = max(rightMax, height[r])
                r -= 1
        return totalWater
