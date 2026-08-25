class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        st_num = set(nums)
        nk = k
        while nk in st_num:
            nk += k
        return nk