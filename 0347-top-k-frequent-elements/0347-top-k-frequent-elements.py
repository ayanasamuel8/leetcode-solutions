class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        cntr = Counter(nums)
        for key, value in cntr.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for value, key in heap]