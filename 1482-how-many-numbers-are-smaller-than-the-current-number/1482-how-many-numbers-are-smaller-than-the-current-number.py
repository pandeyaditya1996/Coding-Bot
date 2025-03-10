class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        temp = sorted(nums)
        store = dict()

        for idx, elem in enumerate(temp):
            if elem not in store:
                store[elem] = idx

        res = []
        for num in nums:
            res.append(store[num])

        return res