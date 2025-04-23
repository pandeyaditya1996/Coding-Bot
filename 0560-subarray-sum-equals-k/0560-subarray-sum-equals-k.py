class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        store = {0:1}
        tot = 0
        ans = 0
        for num in nums:
            tot+=num
            if tot-k in store:
                ans+=store[tot-k]
            store[tot] = store.get(tot, 0) + 1

        return ans
