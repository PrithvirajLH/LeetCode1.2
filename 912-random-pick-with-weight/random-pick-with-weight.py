class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = []
        total = 0

        for weight in w:
            total += weight
            self.prefixSum.append(total)
        
        self.total = total
        

    def pickIndex(self) -> int:
        target = random.uniform(0,self.total)
        l, r = 0, len(self.prefixSum)

        while l < r:
            m = (l + r )// 2

            if self.prefixSum[m] < target:
                l = m + 1
            else:
                r = m  
            
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()