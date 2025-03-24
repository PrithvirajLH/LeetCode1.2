class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        count  = Counter(nums)
        outlier = float('-inf')
        for num in nums:
            total_sum -= num
            count[num] -= 1

            if total_sum % 2 == 0 and count[total_sum//2] > 0:
                outlier = max(outlier, num)
            
            total_sum += num
            count[num] += 1
        return outlier

        