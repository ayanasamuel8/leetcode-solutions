class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        cnt = 2
        inc = True
        n = len(nums)
        p = q = 0
        for i in range(1, n):
            if nums[i] == nums[i -1]:
                return False
            if inc and nums[i] < nums[i - 1]:
                cnt -= 1
                inc = not inc
                p = i - 1
            elif not inc and nums[i] > nums[i - 1]:
                cnt -= 1
                inc = not inc
                q = i - 1
            if cnt < 0:
                return False
        if p == n- 1 or q == n-1 or p == 0 or q == 0:
            return False
        return True