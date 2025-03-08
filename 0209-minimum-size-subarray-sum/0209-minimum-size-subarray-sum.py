class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ans = float('inf')
        curr = 0
        left = 0
        checked = False
        for right in range(len(nums)):
            curr+=nums[right]
            if curr<target:
                continue
            checked = True
            while(curr>=target):
                curr-=nums[left]
                ans = min(ans, right-left+1)
                left+=1
        return ans if checked else 0
            
