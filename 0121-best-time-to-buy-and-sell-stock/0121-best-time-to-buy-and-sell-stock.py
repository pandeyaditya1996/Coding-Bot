class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = float('-inf')
        high = float('-inf')
        for price in prices[::-1]:
            high = max(high, price)
            ans = max(ans, high - price)

        return ans