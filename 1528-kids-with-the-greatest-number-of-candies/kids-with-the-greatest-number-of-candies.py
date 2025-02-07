class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc = candies[0]
        for candy in candies:
            if candy > maxc:
                maxc = candy
        res = []
        for candy in candies:
            if candy + extraCandies >= maxc:
                res.append(True)
            else:
                res.append(False)
        return res
        