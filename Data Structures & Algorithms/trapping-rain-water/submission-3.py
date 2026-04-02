class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        prefix = 0
        maxPrefix = [0 for i in range(len(height))]
        for i in range(len(maxPrefix)):
            maxPrefix[i] = prefix
            prefix = max(prefix, height[i])

        postfix = 0
        for i in range(len(maxPrefix) - 1, -1, -1):
            maxPrefix[i] = min(maxPrefix[i], postfix)
            postfix = max(height[i], postfix)

        maxRain = 0
        for i in range(len(height)):
            if height[i] < maxPrefix[i]:
                maxRain += maxPrefix[i] - height[i]
        return maxRain