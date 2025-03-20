class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        count = Counter(nums)

        for num, freq in count.items():
            heapq.heappush(max_heap, (freq, num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [val for _, val in max_heap]
        