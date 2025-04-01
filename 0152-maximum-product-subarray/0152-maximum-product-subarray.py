class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        left_prod = 1
        max_prod = float('-inf')

        for num in nums:
            left_prod*=num
            max_prod = max(max_prod, left_prod)
            if num==0:
                left_prod = 1

        right_prod = 1
        for num in nums[::-1]:
            right_prod*=num
            max_prod = max(max_prod, right_prod)
            if num==0:
                right_prod = 1

        return max_prod
