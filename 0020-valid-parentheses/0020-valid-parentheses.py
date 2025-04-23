class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        mapper = {"}":"{",")":"(","]":"["}
        for i in s:
            if i in "({[":
                stk.append(i)
            else:
                if not stk or mapper[i]!=stk[-1]:
                    return False
                stk.pop()
        return not stk