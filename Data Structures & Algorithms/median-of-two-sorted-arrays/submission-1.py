class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []

        i, i2 = 0, 0
        while i < len(nums1) and i2 < len(nums2):
            if nums1[i] < nums2[i2]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[i2])
                i2 += 1
        
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1
        while i2 < len(nums2):
            nums3.append(nums2[i2])
            i2 += 1
        
        med1 = (len(nums3) - 1) // 2
        med2 = 0
        if len(nums3) % 2 == 0:
            med2 = med1 + 1
            return (nums3[med1] + nums3[med2]) / 2
        else:
            return nums3[med1]