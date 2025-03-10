class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        store = dict()

        for idx,num in enumerate(nums):

            if num in store:
                if idx-store[num]<=k:
                    return True
            store[num] = idx

        return False