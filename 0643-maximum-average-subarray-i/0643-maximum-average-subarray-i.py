class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        tot = 0

        for i in range(k):
            tot+=nums[i]

        max_avg = tot/k

        for i in range(k, len(nums)):
            tot+=nums[i]-nums[i-k]
            max_avg = max(max_avg, tot/k)

        return max_avg