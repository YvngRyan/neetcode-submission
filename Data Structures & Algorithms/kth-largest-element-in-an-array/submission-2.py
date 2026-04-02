class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxNums = [-n for n in nums]
        heapq.heapify(maxNums)

        while k > 1:
            heapq.heappop(maxNums)
            k -= 1
        return -(maxNums[0])