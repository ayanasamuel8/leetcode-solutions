class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ss = set()

        def unpacked(num):
            ret = set()
            num = str(num)
            for i in range(1, len(num)+1):
                ret.add(num[:i])
            return ret

        n, m = len(arr1), len(arr2)
        for i in range(n):
            ss.update(unpacked(arr1[i]))
        
        max_=0
        for i in range(m):
            for j in unpacked(arr2[i]):
                if j in ss:
                    max_ = max(max_, len(j))
        return max_