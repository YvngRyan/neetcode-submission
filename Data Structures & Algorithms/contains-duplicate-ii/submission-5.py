class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = set()
        i, j = 0, 1
        count.add(nums[i])

        while j < len(nums):
            while (j - i) > k:
                count.remove(nums[i])
                i += 1

            if nums[j] in count:
                return True
            count.add(nums[j])
            j += 1
        return False