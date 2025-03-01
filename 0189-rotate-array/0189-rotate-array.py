class Solution:

    def reverse(self, seq, start, stop):
        size = stop + start
        for i in range(start, (size + 1) // 2):
            j = size - i
            seq[i], seq[j] = seq[j], seq[i]


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k%len(nums)
        
        nums.reverse()
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)