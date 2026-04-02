class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        
        for num in nums:
            if num in dictionary:
                return True
            else:
                dictionary[num] = 1
        return False