
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        ideal = 0
        actual = 0
        n = len(nums)
        for i in range(0, n+1):
            ideal = ideal ^ i
        for num in nums:
            actual = actual ^ num
        return ideal ^ actual


        