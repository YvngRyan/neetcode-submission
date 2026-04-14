class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]

        mp = defaultdict(int)

        for n in nums:
            mp[n] += 1
        
        for key, val in mp.items():
            count[val].append(key)
        
        res = []
        for i in range(len(count) - 1, -1, -1):
            for n in count[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
