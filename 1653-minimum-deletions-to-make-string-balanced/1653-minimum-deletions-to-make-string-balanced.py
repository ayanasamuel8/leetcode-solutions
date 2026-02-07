class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_sum,a_sum=0,0
        for i in s:
            a_sum+=i=='a'
        min_deletion=len(s)
        for i in s:
            min_deletion=min(min_deletion,b_sum+a_sum)
            b_sum+=i=='b'
            a_sum-=i=='a'
        min_deletion=min(min_deletion,b_sum+a_sum)
        return min_deletion