class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        mp = defaultdict(list)
        
        for i, v in enumerate(nums):
            mp[v].append(i)
        
        ans = []
        for q in queries:
            ans.append(inf)
            val = nums[q]
            if len(mp[val]) > 1:
                idx = bisect_left(mp[val], q)
                if idx > 0:
                    ans[-1] = mp[val][idx] - mp[val][idx - 1]
                else:
                    ans[-1] = mp[val][idx] + len(nums) - mp[val][-1]
                if idx < len(mp[val]) - 1:
                    ans[-1] = min(ans[-1], mp[val][idx + 1] - mp[val][idx])
                else:
                    ans[-1] = min(ans[-1], len(nums) - mp[val][idx] + mp[val][0])
        return [i if i != inf else -1 for i in ans]