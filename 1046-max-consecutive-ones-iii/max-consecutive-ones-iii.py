class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        num_zero = 0
        max_size  = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zero += 1
            
            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1
            
            size = r - l + 1

            max_size = max(max_size, size)
        return max_size


        