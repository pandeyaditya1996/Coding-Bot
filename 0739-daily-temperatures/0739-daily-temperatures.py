class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        ans = [0] * n
        stk = []

        for i,t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                stk_temp, stk_idx = stk.pop()
                ans[stk_idx] = i - stk_idx

            stk.append((t,i))

        return ans