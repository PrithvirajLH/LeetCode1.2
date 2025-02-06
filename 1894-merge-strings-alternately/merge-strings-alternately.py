class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        res = ""
        if len(word1) < len(word2):
            i = 0
            while i < len(word1):
                res += word1[i]
                res += word2[i]
                i += 1
            res += word2[i:]
        else:
            i = 0
            while i < len(word2):
                res += word1[i]
                res += word2[i]
                i += 1
            res += word1[i:]
        return res 
