class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        total = 0

        while l <= r:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, height[l])
                total += (maxLeft - height[l])
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                total += (maxRight - height[r])
                r -= 1
        return total