class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ans = []
        l = 0
        r = len(nums) - 1

        op = [0 for _ in range(len(nums))]
        pos = len(nums) - 1
        while(l<=r):
            if abs(nums[l])>abs(nums[r]):
                op[pos] = nums[l]*nums[l]
                l+=1
            else:
                op[pos] = nums[r]*nums[r]
                r-=1 
            pos-=1

        return op

            
            