class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        def check(pas):
            if len(pas) == n:
                if pas not in nums:
                    return pas
                else:
                    return -1
            zero = check(pas + '0')
            if zero != -1:
                return zero
            one = check(pas + '1')
            return one
        return check('')