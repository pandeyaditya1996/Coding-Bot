class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while(l<r):
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
                    r-=1
                elif threeSum>0:
                    r-=1
                else:
                    l+=1

        return ans