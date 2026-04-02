class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashM:
                return[hashM[diff], i]
            hashM[nums[i]] = i
        return -1