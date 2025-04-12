import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def check(num, piles):
            total = 0
            for elem in piles:
                total+=math.ceil(elem/num)
                if total>h:
                    return False
            print('T', num, total)
            return True

        piles.sort()
        l = 1
        r = piles[-1]
        ans = r
        while(l<=r):
            mid = (l+r)//2
            stat = check(mid, piles)
            print(mid, stat)
            if not stat:
                l = mid+1
            else:
                ans = min(ans, mid)
                r = mid - 1

        return ans
