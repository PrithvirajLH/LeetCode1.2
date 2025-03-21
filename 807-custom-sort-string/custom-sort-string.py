class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq_map = Counter(s)
        res = []

        for c in order:
            if c in freq_map:
                res.extend([c] * freq_map[c])

                del freq_map[c]
        
        for c, freq in freq_map.items():
            res.extend([c]*freq)
        
        return "".join(res)