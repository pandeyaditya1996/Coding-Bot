class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:  

        store = {0:1}
        prefixSum = 0
        ans = 0
        for num in nums:
            prefixSum+=num
            if prefixSum - k in store:
                ans+=store[prefixSum-k]
            store[prefixSum]= store.get(prefixSum, 0) + 1
        return ans