class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        def merge(word1, word2, num):
            res = ""
            i = 0
            while i < num:
                res += word1[i] + word2[i]
                i += 1
            res += word1[i:] + word2[i:]
            return res
        
        return merge(word1, word2, min(len(word1), len(word2)))


        