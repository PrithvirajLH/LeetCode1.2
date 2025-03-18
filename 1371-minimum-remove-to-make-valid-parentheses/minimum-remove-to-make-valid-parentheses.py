class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0

        for c in s:
            if c == "(":
                res.append(c)
                count += 1
            elif c == ")" and count > 0:
                res.append(c)
                count -= 1
            elif c != ")":
                res.append(c)
        
        ans = []
        for c in res[::-1]:
            if c == "(" and count > 0:
                count -= 1
            else:
                ans.append(c)
        
        return "".join(ans[::-1])

