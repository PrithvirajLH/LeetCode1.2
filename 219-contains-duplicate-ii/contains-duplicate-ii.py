class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_index = defaultdict(list)

        for i, num in enumerate(nums):
            if num in map_index:
                for j in map_index[num]:
                    if i - j <= k:
                        return True 
            map_index[num].append(i)

        return False 
        