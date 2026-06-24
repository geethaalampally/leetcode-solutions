class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m - 1      # 2
        j = n - 1      # 2
        idx = m + n - 1  # 5

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1

            idx -= 1

        # Copy remaining elements of nums2
        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1
        
