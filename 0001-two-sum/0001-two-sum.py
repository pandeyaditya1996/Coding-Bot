class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = dict()
        for idx,elem in enumerate(nums):
            if target - elem in store:
                return [idx, store[target- elem]]
            store[elem] = idx
