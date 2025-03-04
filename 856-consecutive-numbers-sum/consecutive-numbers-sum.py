class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0

        for k in range(1,n):
            x = n/ (k+1) - k/2
            if x <= 0: break
            if x == int(x):
                count += 1
        
        return count+1