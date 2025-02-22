class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        store = dict()
        l = 0
        r = len(nums) - 1
        for num in nums:
            if num not in store:
                store[num] = ""
        i = 0
        for x,y in store.items():
            nums[i] = x
            i+=1
        return len(store)