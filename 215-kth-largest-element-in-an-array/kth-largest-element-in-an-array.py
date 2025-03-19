class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        for _ in range(k-1):
            res = heapq.heappop(max_heap)
        
        return -heapq.heappop(max_heap)
        