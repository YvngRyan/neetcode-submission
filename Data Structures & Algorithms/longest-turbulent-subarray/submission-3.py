class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxTurbulenceSize = 1
        prevComparison = None
        l = 0

        for r in range(1, len(arr)):
            #If Equal
            if arr[r] == arr[r - 1]:
                l = r
                prevComparison = None
                continue

            # If there has been no comparisons yet
            if prevComparison == None:
                if arr[r] > arr[r - 1]:
                    prevComparison = "more"
                elif arr[r] < arr[r - 1]:
                    prevComparison = "less"
                maxTurbulenceSize = max(maxTurbulenceSize, r - l + 1)
                continue

            # standard case
            if arr[r] > arr[r - 1] and prevComparison == "less":
                prevComparison = "more"
                maxTurbulenceSize = max(maxTurbulenceSize, r - l + 1)
            elif arr[r] < arr[r - 1] and prevComparison == "more":
                prevComparison = "less"
                maxTurbulenceSize = max(maxTurbulenceSize, r - l + 1)
            else:
                l = r - 1
                prevComparison = "more" if arr[r] > arr[r - 1] else "less"
    
        return maxTurbulenceSize