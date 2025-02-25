class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            while(l<r):
                total = nums[l] + nums[r]
                if total+nums[i]==0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif total+nums[i]>0:
                    r-=1
                else:
                    l+=1
        return list(map(list, ans))
                
