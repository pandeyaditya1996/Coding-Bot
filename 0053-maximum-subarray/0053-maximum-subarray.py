class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = float('-inf')
        maxSum = float('-inf')

        for num in nums:
            if currSum<0 and num>currSum:
                currSum = num
            else:
                currSum+=num
            maxSum = max(currSum, maxSum)

        return maxSum