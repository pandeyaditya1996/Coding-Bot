class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        high = float('-inf')
        ans = float('-inf')

        for price in prices[::-1]:
            high = max(high, price)
            ans = max(ans, high - price)        

        return ans