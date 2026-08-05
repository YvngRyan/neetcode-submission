class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Cpy = nums1[:m]

        idx = 0
        i, j = 0, 0

        while i < m or j < n:
            if j >= n or (i < m and nums1Cpy[i] < nums2[j]):
                nums1[idx] = nums1Cpy[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1
        

        # while i < m:
        #     nums1[idx] = nums1Cpy[i]
        #     i += 1
        #     idx += 1
        # while j < n:
        #     nums1[idx] = nums2[j]
        #     j += 1
        #     idx += 1