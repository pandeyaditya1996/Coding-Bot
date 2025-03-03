class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        store = {}

        for i,num in enumerate(nums):
            if num in store:
                if abs(i-store[num])<=k:
                    return True
            store[num] = i

        return False