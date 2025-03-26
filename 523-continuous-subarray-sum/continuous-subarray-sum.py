class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixMod = {0 : -1}
        total = 0

        for i, n in enumerate(nums):
            total += n
            remainder = total % k
            if remainder not in prefixMod:
                prefixMod[remainder] = i
            elif i - prefixMod[remainder] > 1:
                return True

        return False 
        