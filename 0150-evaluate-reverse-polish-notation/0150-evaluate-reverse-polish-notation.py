class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def func(x, y, token):
            mapper = {
                "+": lambda x,y:x+y,
                "-": lambda x,y:x-y,
                "*": lambda x,y:x*y,
                "/": lambda x,y:x/y,
            }
            return int(mapper[token](x,y))

        stk = []
        ans = 0
        for token in tokens:
            if token not in "+-*/":
                stk.append(int(token))
            else:
                second = stk.pop()
                first = stk.pop()
                stk.append(func(first, second, token))

        return stk[-1]