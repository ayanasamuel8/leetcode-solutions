class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        for num in nums1:
            if num % 2 != 0:
                break
        else:
            return True
        if min(nums1) % 2 == 0:
            return False
        return True