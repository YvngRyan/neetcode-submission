class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numIndex:
                return [numIndex[diff], i]
            numIndex[nums[i]] = i
        return []