class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(sign, num):
            if sign == "+": stack.append(num)
            if sign == "-": stack.append(-num)
            if sign == "*": stack.append(stack.pop()*num)
            if sign == "/": stack.append(int(stack.pop() / num))

        i = 0
        num = 0
        stack = []
        sign = "+"

        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] in "+-*/":
                evaluate(sign, num)
                num = 0
                sign = s[i]
            i += 1
        evaluate(sign, num)
        return sum(stack)