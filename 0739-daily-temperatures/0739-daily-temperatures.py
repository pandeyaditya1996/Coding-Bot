class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stk = []
        ans = [0] * n

        for idx,temp in enumerate(temperatures):
            while stk and stk[-1][0] < temp:
                stk_temp, stk_idx = stk.pop()
                ans[stk_idx] = idx - stk_idx

            stk.append((temp, idx))

        return ans