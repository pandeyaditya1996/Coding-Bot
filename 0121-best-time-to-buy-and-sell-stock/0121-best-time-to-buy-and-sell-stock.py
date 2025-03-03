class Solution:
    def maxProfit(self, nums: List[int]) -> int:

        high = 0
        ans = 0
        for num in nums[::-1]:
            high = max(num, high)
            ans = max(ans, high - num)
        return ans
        