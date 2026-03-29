class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        odd = []
        even = []
        odd2 = []
        even2 = []
        for i in range(len(s1)):
            if i % 2:
                odd.append(s1[i])
                odd2.append(s2[i])
            else:
                even.append(s1[i])
                even2.append(s2[i])
        odd.sort()
        even.sort()
        odd2.sort()
        even2.sort()
        return odd == odd2 and  even == even2
        