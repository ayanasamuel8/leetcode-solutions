class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        doub = set()
        trip = set()
        n = len(nums)
        for i in range(n):
            for j in range(n):
                doub.add(nums[i] ^ nums[j])
        for i in range(n):
            for j in doub:
                trip.add(nums[i] ^ j)
        return len(trip)