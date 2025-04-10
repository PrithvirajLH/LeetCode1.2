class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_ransom = Counter(ransomNote)
        map_magazine = Counter(magazine)

        for c in set(ransomNote):
            if map_ransom[c] > map_magazine[c]:
                return False
        
        return True