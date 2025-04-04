class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = ""
        stack = []

        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack: stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""            
            else:
                curr += c
        return "/" + "/".join(stack)
        