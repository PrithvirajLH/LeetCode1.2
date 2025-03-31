class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        maxSize = 0
        seen = set()
        for r in range(len(s)):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1                
                l += 1
            else:
                seen.add(s[r])
            maxSize = max(maxSize, (r-l) + 1)

        return maxSize