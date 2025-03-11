class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = float('-inf')
        left_prod = 1
        for num in nums:
            left_prod*= num
            ans = max(ans, left_prod)
            if num == 0:
                left_prod = 1

        right_prod = 1
        for num in nums[::-1]:
            right_prod*= num
            ans = max(ans, right_prod)
            if num == 0:
                right_prod = 1

        return ans

