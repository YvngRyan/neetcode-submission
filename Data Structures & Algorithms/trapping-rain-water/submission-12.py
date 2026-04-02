class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        maxRight = 0
        maxLeft = 0

        total = 0
        while l <= r:
            if maxLeft < maxRight:
                total += max(0, maxLeft - height[l])
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                total += max(0, maxRight - height[r])
                maxRight = max(maxRight, height[r])
                r -= 1
        return total

            