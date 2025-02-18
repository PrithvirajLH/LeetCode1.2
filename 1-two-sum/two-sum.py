class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, val in enumerate(nums):
            diff = target - val

            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[val] = i
        