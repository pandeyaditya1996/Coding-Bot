# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        l = 1
        r = n

        while(l<=r):
            mid = (l + r)//2
            if isBadVersion(mid)==False:
                l = mid + 1
            else:
                r = mid - 1

        return mid if isBadVersion(mid) else mid+1

        