class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)

        hash_map = {}

        for i, val in enumerate(temp):
            if val not in hash_map:
                hash_map[val] = i

        res = []
        for i in nums:
            res.append(hash_map[i])

        return res 