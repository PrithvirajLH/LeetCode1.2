class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map_text = Counter(text)
        min_count = len(text)
        for c in "ban":
            min_count = min(min_count, map_text[c])
        
        double_letter = min(map_text["l"], map_text["o"])

        while 2*min_count > double_letter:
            min_count -= 1
        
        return min_count

        