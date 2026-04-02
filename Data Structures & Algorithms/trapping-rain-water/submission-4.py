class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]
        total = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft)
                total += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                total += maxRight - height[r]
        return total