class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for idx,num in enumerate(nums):
            if target-num in store:
                return [idx, store[target-num]]
            store[num] = idx
        
        