class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        bracket_map = {')':'(',"}":"{","]":"["}
        for char in s:
            if char in '({[':
                stk.append(char)
            else:
                if not stk or stk[-1]!=bracket_map.get(char):
                    return False
                stk.pop()
        return not stk