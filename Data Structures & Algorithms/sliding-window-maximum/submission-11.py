class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        q = collections.deque()

        res = []

        while r < k:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            r += 1
        res.append(nums[q[0]])
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            r += 1
            l += 1

            while q and q[0] < l:
                q.popleft()
            
            res.append(nums[q[0]])
        return res

# k = 3
# nums[1,2,1,0,4,2,6]

# q = [1]
# res = []
# l = 0
# r = 2