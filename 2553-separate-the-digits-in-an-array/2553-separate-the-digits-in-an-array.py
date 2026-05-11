class Solution:
    def sep(self, num):
        arr =[]
        while num:
            arr.append(num%10)
            num//=10
        return arr[::-1]
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.extend(self.sep(i))
        return ans