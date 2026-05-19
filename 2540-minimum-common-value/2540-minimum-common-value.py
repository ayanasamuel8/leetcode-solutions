class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = right = 0
        n, m = len(nums1), len(nums2)
        while left < n and right < m:
            if nums1[left] == nums2[right]:
                return nums1[left]
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                left += 1
        return -1