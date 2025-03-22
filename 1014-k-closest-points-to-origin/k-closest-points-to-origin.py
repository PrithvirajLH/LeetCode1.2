class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            heapq.heappush(minHeap, [dist, x, y])
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        
        return res

        