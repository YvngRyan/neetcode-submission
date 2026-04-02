class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        mp = {}

        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        for key, val in mp.items():
            count[val].append(key)

        res = []
        for i in range(len(count) - 1, -1, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

        