class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        start = 0
        ans = float('inf')

        for i in range(len(nums)):
            currSum += nums[i]
            while currSum >= target and start < len(nums):
                ans = min(ans, i-start+1)
                currSum -= nums[start]
                start += 1
        return 0 if ans == float('inf') else ans
 

        