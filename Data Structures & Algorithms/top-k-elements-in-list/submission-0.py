class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            dictionary[num] = 1 + dictionary.get(num, 0)
        
        for key, value in dictionary.items():
            freq[value].append(key)

        res_array = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res_array.append(num)
                if len(res_array) == k:
                    return res_array
        