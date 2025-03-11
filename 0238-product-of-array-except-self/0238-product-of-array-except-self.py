class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prod = 1
        right_prod = 1

        op = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            op[i] = left_prod
            left_prod*=nums[i]

        for i in range(len(nums) - 1, -1, -1):
            op[i]*= right_prod
            right_prod*=nums[i]

        return op