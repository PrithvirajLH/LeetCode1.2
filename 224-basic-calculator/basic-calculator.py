class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            # if op == "*": stack.append(stack.pop()*v)
            # if op == "/": stack.append(int(stack.pop()/v))

        i = 0 
        num = 0
        stack = []
        sign = '+'

        while i < len(s):
            if s[i].isdigit():
                num = (num * 10) + int(s[i])
            elif s[i] in "+-":
                evaluate(sign, num)
                num = 0
                sign = s[i]
            elif s[i] == "(":
                num, j = self.calculate(s[i+1:])
                i = i + j
            elif s[i] == ")":
                evaluate(sign, num)
                return sum(stack), i + 1
            i += 1
        evaluate(sign, num)
        return sum(stack)
        

        