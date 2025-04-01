class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 0
        while k != 0:
            ans += 1
            if ans not in arr:
                k -= 1
        return ans
        