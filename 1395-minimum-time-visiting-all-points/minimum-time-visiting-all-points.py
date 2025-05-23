class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0

        x1, y1 = points.pop()

        while points:
            x2, y2 = points.pop()
            dist = max( abs(x2 - x1), abs(y2 - y1))
            res += dist
            x1, y1 = x2, y2
        
        return res

