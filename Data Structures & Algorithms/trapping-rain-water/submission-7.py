class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute Force: [.., .., ..]


        minHeightsOfSides = [0] * len(height)

        prefixMax = 0
        for i in range(len(height)):
            minHeightsOfSides[i] = prefixMax
            prefixMax = max(prefixMax, height[i])
        
        postfixMax = 0
        for i in range(len(height) - 1, -1, -1):
            minHeightsOfSides[i] = min(minHeightsOfSides[i], postfixMax)
            postfixMax = max(postfixMax, height[i])
        
        total = 0
        for i in range(len(height)):
            if height[i] < minHeightsOfSides[i]:
                total += minHeightsOfSides[i] - height[i]
        return total

        # postfix = 3
        # [0, 0, 2, 2, 3, 3, 3, 2, 1, 0]

        