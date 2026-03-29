class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        half = (n1 + n2 + 1) // 2

        # [l, r] on how many elements we take from nums1
        l, r = 0, n1
        while l <= r:
            m1 = l + (r - l) // 2       # take m1 elements from nums1
            m2 = half - m1               # take the rest from nums2

            # Edge cases: if partition is at boundary, use -inf/inf
            left1  = nums1[m1 - 1] if m1 > 0  else float('-inf')
            left2  = nums2[m2 - 1] if m2 > 0  else float('-inf')
            right1 = nums1[m1]     if m1 < n1  else float('inf')
            right2 = nums2[m2]     if m2 < n2  else float('inf')

            if left1 <= right2 and left2 <= right1:
                # Valid partition found
                if (n1 + n2) % 2 == 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                r = m1 - 1               # took too many from nums1
            else:
                l = m1 + 1               # took too few from nums1